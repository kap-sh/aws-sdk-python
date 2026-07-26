"""Generated from Smithy shape ``com.amazonaws.appmesh#WeightedTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.weighted_target

WeightedTargets: TypeAlias = list["capo_app_mesh.types.weighted_target.WeightedTarget"]


# --- restJson1 ser/de ---
def serialize_json(value: WeightedTargets) -> list:
    import capo_app_mesh.types.weighted_target

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.weighted_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> WeightedTargets:
    import capo_app_mesh.types.weighted_target

    out: WeightedTargets = []
    for item in data:
        out.append(capo_app_mesh.types.weighted_target.deserialize_json(item))
    return out
