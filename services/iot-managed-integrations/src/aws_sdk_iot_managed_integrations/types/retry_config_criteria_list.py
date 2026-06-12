"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RetryConfigCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.retry_config_criteria

RetryConfigCriteriaList: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.retry_config_criteria.RetryConfigCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetryConfigCriteriaList) -> list:
    import aws_sdk_iot_managed_integrations.types.retry_config_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.retry_config_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RetryConfigCriteriaList:
    import aws_sdk_iot_managed_integrations.types.retry_config_criteria

    out: RetryConfigCriteriaList = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.retry_config_criteria.deserialize_json(
                item
            )
        )
    return out
