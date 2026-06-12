"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SceneSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.s3_url
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class SceneSummary(TypedDict):
    scene_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the scene.</p>"""
    content_location: "aws_sdk_iottwinmaker.types.s3_url.S3Url"
    """<p>The relative path that specifies the location of the content definition file.</p>"""
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the scene.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was created.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was last updated.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The scene description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SceneSummary) -> dict:
    out: dict = {}
    out["sceneId"] = value["scene_id"]
    out["contentLocation"] = value["content_location"]
    out["arn"] = value["arn"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SceneSummary:
    out: SceneSummary = {}  # type: ignore[typeddict-item]
    if "sceneId" in data:
        out["scene_id"] = data["sceneId"]
    else:
        raise DeserializationError("SceneSummary.scene_id required")
    if "contentLocation" in data:
        out["content_location"] = data["contentLocation"]
    else:
        raise DeserializationError("SceneSummary.content_location required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SceneSummary.arn required")
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError("SceneSummary.creation_date_time required")
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("SceneSummary.update_date_time required")
    if "description" in data:
        out["description"] = data["description"]
    return out
