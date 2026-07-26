"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RetryConfigCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.retry_config_criteria

RetryConfigCriteriaList: TypeAlias = list[
    "capo_iot_managed_integrations.types.retry_config_criteria.RetryConfigCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetryConfigCriteriaList) -> list:
    import capo_iot_managed_integrations.types.retry_config_criteria

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.retry_config_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RetryConfigCriteriaList:
    import capo_iot_managed_integrations.types.retry_config_criteria

    out: RetryConfigCriteriaList = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.retry_config_criteria.deserialize_json(
                item
            )
        )
    return out
