"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_config

HoursOfOperationConfigList: TypeAlias = list[
    "aws_sdk_connect.types.hours_of_operation_config.HoursOfOperationConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationConfigList) -> list:
    import aws_sdk_connect.types.hours_of_operation_config

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.hours_of_operation_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> HoursOfOperationConfigList:
    import aws_sdk_connect.types.hours_of_operation_config

    out: HoursOfOperationConfigList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.hours_of_operation_config.deserialize_json(item)
        )
    return out
