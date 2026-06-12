"""Generated from Smithy shape ``com.amazonaws.pipes#PlacementConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.placement_constraint

PlacementConstraints: TypeAlias = list[
    "aws_sdk_pipes.types.placement_constraint.PlacementConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlacementConstraints) -> list:
    import aws_sdk_pipes.types.placement_constraint

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.placement_constraint.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlacementConstraints:
    import aws_sdk_pipes.types.placement_constraint

    out: PlacementConstraints = []
    for item in data:
        out.append(aws_sdk_pipes.types.placement_constraint.deserialize_json(item))
    return out
