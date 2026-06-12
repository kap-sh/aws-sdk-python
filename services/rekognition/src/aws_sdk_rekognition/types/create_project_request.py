"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateProjectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.customization_feature
    import aws_sdk_rekognition.types.project_auto_update
    import aws_sdk_rekognition.types.project_name
    import aws_sdk_rekognition.types.tag_map


class CreateProjectRequest(TypedDict):
    project_name: "aws_sdk_rekognition.types.project_name.ProjectName"
    """<p>The name of the project to create.</p>"""
    feature: NotRequired[
        "aws_sdk_rekognition.types.customization_feature.CustomizationFeature"
    ]
    """<p>Specifies feature that is being customized. If no value is provided CUSTOM_LABELS is used as a default.</p>"""
    auto_update: NotRequired[
        "aws_sdk_rekognition.types.project_auto_update.ProjectAutoUpdate"
    ]
    """<p>Specifies whether automatic retraining should be attempted for the versions of the project. Automatic retraining is done as a best effort. Required argument for Content Moderation. Applicable only to adapters.</p>"""
    tags: NotRequired["aws_sdk_rekognition.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that you want to attach to the project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectRequest) -> dict:
    out: dict = {}
    out["ProjectName"] = value["project_name"]
    if "feature" in value:
        import aws_sdk_rekognition.types.customization_feature

        out["Feature"] = (
            aws_sdk_rekognition.types.customization_feature.serialize_aws_json_1_1(
                value["feature"]
            )
        )
    if "auto_update" in value:
        import aws_sdk_rekognition.types.project_auto_update

        out["AutoUpdate"] = (
            aws_sdk_rekognition.types.project_auto_update.serialize_aws_json_1_1(
                value["auto_update"]
            )
        )
    if "tags" in value:
        import aws_sdk_rekognition.types.tag_map

        out["Tags"] = aws_sdk_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectRequest:
    out: CreateProjectRequest = {}  # type: ignore[typeddict-item]
    if "ProjectName" in data:
        out["project_name"] = data["ProjectName"]
    else:
        raise DeserializationError("CreateProjectRequest.project_name required")
    if "Feature" in data:
        import aws_sdk_rekognition.types.customization_feature

        out["feature"] = (
            aws_sdk_rekognition.types.customization_feature.deserialize_aws_json_1_1(
                data["Feature"]
            )
        )
    if "AutoUpdate" in data:
        import aws_sdk_rekognition.types.project_auto_update

        out["auto_update"] = (
            aws_sdk_rekognition.types.project_auto_update.deserialize_aws_json_1_1(
                data["AutoUpdate"]
            )
        )
    if "Tags" in data:
        import aws_sdk_rekognition.types.tag_map

        out["tags"] = aws_sdk_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
