"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetSceneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.generated_scene_metadata_map
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.s3_url
    import capo_iottwinmaker.types.scene_capabilities
    import capo_iottwinmaker.types.scene_error
    import capo_iottwinmaker.types.scene_metadata_map
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class GetSceneResponse(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the scene.</p>"""
    scene_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the scene.</p>"""
    content_location: "capo_iottwinmaker.types.s3_url.S3Url"
    """<p>The relative path that specifies the location of the content definition file.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the scene.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was created.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was last updated.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the scene.</p>"""
    capabilities: NotRequired[
        "capo_iottwinmaker.types.scene_capabilities.SceneCapabilities"
    ]
    """<p>A list of capabilities that the scene uses to render.</p>"""
    scene_metadata: NotRequired[
        "capo_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
    ]
    """<p>The response metadata.</p>"""
    generated_scene_metadata: NotRequired[
        "capo_iottwinmaker.types.generated_scene_metadata_map.GeneratedSceneMetadataMap"
    ]
    """<p>The generated scene metadata.</p>"""
    error: NotRequired["capo_iottwinmaker.types.scene_error.SceneError"]
    """<p>The SceneResponse error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSceneResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["sceneId"] = value["scene_id"]
    out["contentLocation"] = value["content_location"]
    out["arn"] = value["arn"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "capabilities" in value:
        import capo_iottwinmaker.types.scene_capabilities

        out["capabilities"] = capo_iottwinmaker.types.scene_capabilities.serialize_json(
            value["capabilities"]
        )
    if "scene_metadata" in value:
        import capo_iottwinmaker.types.scene_metadata_map

        out["sceneMetadata"] = (
            capo_iottwinmaker.types.scene_metadata_map.serialize_json(
                value["scene_metadata"]
            )
        )
    if "generated_scene_metadata" in value:
        import capo_iottwinmaker.types.generated_scene_metadata_map

        out["generatedSceneMetadata"] = (
            capo_iottwinmaker.types.generated_scene_metadata_map.serialize_json(
                value["generated_scene_metadata"]
            )
        )
    if "error" in value:
        import capo_iottwinmaker.types.scene_error

        out["error"] = capo_iottwinmaker.types.scene_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> GetSceneResponse:
    out: GetSceneResponse = {}  # type: ignore[typeddict-item]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("GetSceneResponse.workspace_id required")
    if "sceneId" in data:
        out["scene_id"] = data["sceneId"]
    else:
        raise DeserializationError("GetSceneResponse.scene_id required")
    if "contentLocation" in data:
        out["content_location"] = data["contentLocation"]
    else:
        raise DeserializationError("GetSceneResponse.content_location required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSceneResponse.arn required")
    if "creationDateTime" in data:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        raise DeserializationError("GetSceneResponse.creation_date_time required")
    if "updateDateTime" in data:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("GetSceneResponse.update_date_time required")
    if "description" in data:
        out["description"] = data["description"]
    if "capabilities" in data:
        import capo_iottwinmaker.types.scene_capabilities

        out["capabilities"] = (
            capo_iottwinmaker.types.scene_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    if "sceneMetadata" in data:
        import capo_iottwinmaker.types.scene_metadata_map

        out["scene_metadata"] = (
            capo_iottwinmaker.types.scene_metadata_map.deserialize_json(
                data["sceneMetadata"]
            )
        )
    if "generatedSceneMetadata" in data:
        import capo_iottwinmaker.types.generated_scene_metadata_map

        out["generated_scene_metadata"] = (
            capo_iottwinmaker.types.generated_scene_metadata_map.deserialize_json(
                data["generatedSceneMetadata"]
            )
        )
    if "error" in data:
        import capo_iottwinmaker.types.scene_error

        out["error"] = capo_iottwinmaker.types.scene_error.deserialize_json(
            data["error"]
        )
    return out
