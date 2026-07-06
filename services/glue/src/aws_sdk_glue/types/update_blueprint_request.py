"""Generated from Smithy shape ``com.amazonaws.glue#UpdateBlueprintRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic512_char_string
    import aws_sdk_glue.types.orchestration_name_string
    import aws_sdk_glue.types.orchestration_s3_location


class UpdateBlueprintRequest(TypedDict, closed=True):
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBlueprintRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["BlueprintLocation"] = value["blueprint_location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBlueprintRequest:
    out: UpdateBlueprintRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateBlueprintRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "BlueprintLocation" in data:
        out["blueprint_location"] = data["BlueprintLocation"]
    else:
        raise DeserializationError("UpdateBlueprintRequest.blueprint_location required")
    return out
