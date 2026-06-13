"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceResourceOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.space_resource_operation

SpaceResourceOperations: TypeAlias = list[
    "aws_sdk_quicksight.types.space_resource_operation.SpaceResourceOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceResourceOperations) -> list:
    import aws_sdk_quicksight.types.space_resource_operation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.space_resource_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SpaceResourceOperations:
    import aws_sdk_quicksight.types.space_resource_operation

    out: SpaceResourceOperations = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.space_resource_operation.deserialize_json(item)
        )
    return out
