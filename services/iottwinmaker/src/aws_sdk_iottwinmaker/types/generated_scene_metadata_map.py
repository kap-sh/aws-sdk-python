"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GeneratedSceneMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.scene_metadata_value

GeneratedSceneMetadataMap: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.scene_metadata_value.SceneMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: GeneratedSceneMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> GeneratedSceneMetadataMap:
    out: GeneratedSceneMetadataMap = {}
    for key, value in data.items():
        out[key] = value
    return out
