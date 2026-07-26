"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SceneCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.scene_capability

SceneCapabilities: TypeAlias = list[
    "capo_iottwinmaker.types.scene_capability.SceneCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: SceneCapabilities) -> list:
    return list(value)


def deserialize_json(data: list) -> SceneCapabilities:
    return list(data)
