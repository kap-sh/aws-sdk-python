"""Generated from Smithy shape ``com.amazonaws.glue#CreateBlueprintRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic512_char_string
    import aws_sdk_glue.types.orchestration_name_string
    import aws_sdk_glue.types.orchestration_s3_location
    import aws_sdk_glue.types.tags_map


class CreateBlueprintRequest(TypedDict):
    name: "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    """<p>The name of the blueprint.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.generic512_char_string.Generic512CharString"
    ]
    """<p>A description of the blueprint.</p>"""
    blueprint_location: (
        "aws_sdk_glue.types.orchestration_s3_location.OrchestrationS3Location"
    )
    """<p>Specifies a path in Amazon S3 where the blueprint is published.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>The tags to be applied to this blueprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBlueprintRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["BlueprintLocation"] = value["blueprint_location"]
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBlueprintRequest:
    out: CreateBlueprintRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateBlueprintRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "BlueprintLocation" in data:
        out["blueprint_location"] = data["BlueprintLocation"]
    else:
        raise DeserializationError("CreateBlueprintRequest.blueprint_location required")
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
