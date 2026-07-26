"""Generated from Smithy shape ``com.amazonaws.storagegateway#AddTagsToResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.resource_arn


class AddTagsToResourceOutput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_storage_gateway.types.resource_arn.ResourceARN"]
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
