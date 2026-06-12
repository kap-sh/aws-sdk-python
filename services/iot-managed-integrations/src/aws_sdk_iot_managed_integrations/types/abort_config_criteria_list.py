"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AbortConfigCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.abort_config_criteria

AbortConfigCriteriaList: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.abort_config_criteria.AbortConfigCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: AbortConfigCriteriaList) -> list:
    import aws_sdk_iot_managed_integrations.types.abort_config_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.abort_config_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AbortConfigCriteriaList:
    import aws_sdk_iot_managed_integrations.types.abort_config_criteria

    out: AbortConfigCriteriaList = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.abort_config_criteria.deserialize_json(
                item
            )
        )
    return out
