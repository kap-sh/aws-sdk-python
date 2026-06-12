"""Generated from Smithy shape ``com.amazonaws.connect#EffectiveHoursOfOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.effective_hours_of_operations

EffectiveHoursOfOperationList: TypeAlias = list[
    "aws_sdk_connect.types.effective_hours_of_operations.EffectiveHoursOfOperations"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveHoursOfOperationList) -> list:
    import aws_sdk_connect.types.effective_hours_of_operations

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.effective_hours_of_operations.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EffectiveHoursOfOperationList:
    import aws_sdk_connect.types.effective_hours_of_operations

    out: EffectiveHoursOfOperationList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.effective_hours_of_operations.deserialize_json(item)
        )
    return out
