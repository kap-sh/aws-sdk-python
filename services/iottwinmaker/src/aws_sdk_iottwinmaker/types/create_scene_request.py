"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateSceneRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.s3_url
    import aws_sdk_iottwinmaker.types.scene_capabilities
    import aws_sdk_iottwinmaker.types.scene_metadata_map
    import aws_sdk_iottwinmaker.types.tag_map


class CreateSceneRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the scene.</p>"""
    scene_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the scene.</p>"""
    content_location: "aws_sdk_iottwinmaker.types.s3_url.S3Url"
    """<p>The relative path that specifies the location of the content definition file.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description for this scene.</p>"""
    capabilities: NotRequired[
        "aws_sdk_iottwinmaker.types.scene_capabilities.SceneCapabilities"
    ]
    """<p>A list of capabilities that the scene uses to render itself.</p>"""
    tags: NotRequired["aws_sdk_iottwinmaker.types.tag_map.TagMap"]
    """<p>Metadata that you can use to manage the scene.</p>"""
    scene_metadata: NotRequired[
        "aws_sdk_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
    ]
    """<p>The request metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSceneRequest) -> dict:
    out: dict = {}
    out["sceneId"] = value["scene_id"]
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
    if "tags" in value:
        import aws_sdk_iottwinmaker.types.tag_map

        out["tags"] = aws_sdk_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    if "scene_metadata" in value:
        import aws_sdk_iottwinmaker.types.scene_metadata_map

        out["sceneMetadata"] = (
            aws_sdk_iottwinmaker.types.scene_metadata_map.serialize_json(
                value["scene_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSceneRequest:
    out: CreateSceneRequest = {}  # type: ignore[typeddict-item]
    if "sceneId" in data:
        out["scene_id"] = data["sceneId"]
    else:
        raise DeserializationError("CreateSceneRequest.scene_id required")
    if "contentLocation" in data:
        out["content_location"] = data["contentLocation"]
    else:
        raise DeserializationError("CreateSceneRequest.content_location required")
    if "description" in data:
        out["description"] = data["description"]
    if "capabilities" in data:
        import aws_sdk_iottwinmaker.types.scene_capabilities

        out["capabilities"] = (
            aws_sdk_iottwinmaker.types.scene_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    if "tags" in data:
        import aws_sdk_iottwinmaker.types.tag_map

        out["tags"] = aws_sdk_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    if "sceneMetadata" in data:
        import aws_sdk_iottwinmaker.types.scene_metadata_map

        out["scene_metadata"] = (
            aws_sdk_iottwinmaker.types.scene_metadata_map.deserialize_json(
                data["sceneMetadata"]
            )
        )
    return out
