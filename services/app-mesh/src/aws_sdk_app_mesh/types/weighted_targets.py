"""Generated from Smithy shape ``com.amazonaws.appmesh#WeightedTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.weighted_target

WeightedTargets: TypeAlias = list[
    "aws_sdk_app_mesh.types.weighted_target.WeightedTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: WeightedTargets) -> list:
    import aws_sdk_app_mesh.types.weighted_target

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.weighted_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> WeightedTargets:
    import aws_sdk_app_mesh.types.weighted_target

    out: WeightedTargets = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.weighted_target.deserialize_json(item))
    return out
