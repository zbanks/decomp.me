import { h } from "preact"
import useSWR from "swr"
import Skeleton from "react-loading-skeleton"

import Select from "../Select"
import * as api from "../api"

export default function CompilerConfigSelect({ value, onChange }) {
    const { data, error } = useSWR("/compiler_configs", api.get, { revalidateOnFocus: false })

    if (error) {
        if (value !== null) {
            onChange(null)
        }

        return <span>{error}</span>
    } else if (data) {
        const validIds = Object.values(data).reduce((sum, configs) => {
            for (const config of configs) {
                sum.push(config.id)
            }

            return sum
        }, [])

        if (!validIds.includes(value)) {
            onChange(validIds[0])
        }

        return <Select onChange={event => onChange(parseInt(event.target.value))}>
            {Object.entries(data).map(([compiler, configs]) => {
                return <optgroup label={compiler}>
                    {configs.map(config => 
                        <option value={config.id} selected={config.id == value}>
                            {compiler} {config.cc_flags}
                        </option>
                    )}
                </optgroup>
            })}
        </Select>
    } else {
        return <Skeleton />
    }
}
