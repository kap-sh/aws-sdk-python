"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_override

HoursOfOperationOverrideList: TypeAlias = list[
    "aws_sdk_connect.types.hours_of_operation_override.HoursOfOperationOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationOverrideList) -> list:
    import aws_sdk_connect.types.hours_of_operation_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.hours_of_operation_override.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HoursOfOperationOverrideList:
    import aws_sdk_connect.types.hours_of_operation_override

    out: HoursOfOperationOverrideList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.hours_of_operation_override.deserialize_json(item)
        )
    return out
