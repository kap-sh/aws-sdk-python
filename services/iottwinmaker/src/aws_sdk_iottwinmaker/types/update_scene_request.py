"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateSceneRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.s3_url
    import aws_sdk_iottwinmaker.types.scene_capabilities
    import aws_sdk_iottwinmaker.types.scene_metadata_map


class UpdateSceneRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the scene.</p>"""
    scene_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the scene.</p>"""
    content_location: NotRequired["aws_sdk_iottwinmaker.types.s3_url.S3Url"]
    """<p>The relative path that specifies the location of the content definition file.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of this scene.</p>"""
    capabilities: NotRequired[
        "aws_sdk_iottwinmaker.types.scene_capabilities.SceneCapabilities"
    ]
    """<p>A list of capabilities that the scene uses to render.</p>"""
    scene_metadata: NotRequired[
        "aws_sdk_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
    ]
    """<p>The scene metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSceneRequest) -> dict:
    out: dict = {}
    if "content_location" in value:
        out["contentLocation"] = value["content_location"]
    if "description" in value:
        out["description"] = value["description"]
    if "capabilities" in value:
        import aws_sdk_iottwinmaker.types.scene_capabilities

        out["capabilities"] = (
            aws_sdk_iottwinmaker.types.scene_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    if "scene_metadata" in value:
        import aws_sdk_iottwinmaker.types.scene_metadata_map

        out["sceneMetadata"] = (
            aws_sdk_iottwinmaker.types.scene_metadata_map.serialize_json(
                value["scene_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSceneRequest:
    out: UpdateSceneRequest = {}  # type: ignore[typeddict-item]
    if "contentLocation" in data:
        out["content_location"] = data["contentLocation"]
    if "description" in data:
        out["description"] = data["description"]
    if "capabilities" in data:
        import aws_sdk_iottwinmaker.types.scene_capabilities

        out["capabilities"] = (
            aws_sdk_iottwinmaker.types.scene_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    if "sceneMetadata" in data:
        import aws_sdk_iottwinmaker.types.scene_metadata_map

        out["scene_metadata"] = (
            aws_sdk_iottwinmaker.types.scene_metadata_map.deserialize_json(
                data["sceneMetadata"]
            )
        )
    return out
