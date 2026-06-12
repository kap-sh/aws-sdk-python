"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationOverrideConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_override_config

HoursOfOperationOverrideConfigList: TypeAlias = list[
    "aws_sdk_connect.types.hours_of_operation_override_config.HoursOfOperationOverrideConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationOverrideConfigList) -> list:
    import aws_sdk_connect.types.hours_of_operation_override_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.hours_of_operation_override_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HoursOfOperationOverrideConfigList:
    import aws_sdk_connect.types.hours_of_operation_override_config

    out: HoursOfOperationOverrideConfigList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.hours_of_operation_override_config.deserialize_json(
                item
            )
        )
    return out
