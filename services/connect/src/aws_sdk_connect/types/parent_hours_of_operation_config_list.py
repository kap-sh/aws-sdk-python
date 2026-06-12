"""Generated from Smithy shape ``com.amazonaws.connect#ParentHoursOfOperationConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.parent_hours_of_operation_config

ParentHoursOfOperationConfigList: TypeAlias = list[
    "aws_sdk_connect.types.parent_hours_of_operation_config.ParentHoursOfOperationConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentHoursOfOperationConfigList) -> list:
    import aws_sdk_connect.types.parent_hours_of_operation_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.parent_hours_of_operation_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ParentHoursOfOperationConfigList:
    import aws_sdk_connect.types.parent_hours_of_operation_config

    out: ParentHoursOfOperationConfigList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.parent_hours_of_operation_config.deserialize_json(
                item
            )
        )
    return out
