"""Generated from Smithy shape ``com.amazonaws.storagegateway#AddTagsToResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.resource_arn


class AddTagsToResourceOutput(TypedDict):
    resource_arn: NotRequired["aws_sdk_storage_gateway.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the resource you want to add tags to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceOutput:
    out: AddTagsToResourceOutput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    return out
