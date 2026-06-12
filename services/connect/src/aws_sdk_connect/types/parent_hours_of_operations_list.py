"""Generated from Smithy shape ``com.amazonaws.connect#ParentHoursOfOperationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operations_identifier

ParentHoursOfOperationsList: TypeAlias = list[
    "aws_sdk_connect.types.hours_of_operations_identifier.HoursOfOperationsIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentHoursOfOperationsList) -> list:
    import aws_sdk_connect.types.hours_of_operations_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.hours_of_operations_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ParentHoursOfOperationsList:
    import aws_sdk_connect.types.hours_of_operations_identifier

    out: ParentHoursOfOperationsList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.hours_of_operations_identifier.deserialize_json(item)
        )
    return out
