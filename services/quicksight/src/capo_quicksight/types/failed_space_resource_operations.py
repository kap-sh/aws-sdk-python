"""Generated from Smithy shape ``com.amazonaws.quicksight#FailedSpaceResourceOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.failed_space_resource_operation

FailedSpaceResourceOperations: TypeAlias = list[
    "capo_quicksight.types.failed_space_resource_operation.FailedSpaceResourceOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedSpaceResourceOperations) -> list:
    import capo_quicksight.types.failed_space_resource_operation

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.failed_space_resource_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailedSpaceResourceOperations:
    import capo_quicksight.types.failed_space_resource_operation

    out: FailedSpaceResourceOperations = []
    for item in data:
        out.append(
            capo_quicksight.types.failed_space_resource_operation.deserialize_json(item)
        )
    return out
