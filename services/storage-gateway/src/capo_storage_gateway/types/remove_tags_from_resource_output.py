"""Generated from Smithy shape ``com.amazonaws.storagegateway#RemoveTagsFromResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.resource_arn


class RemoveTagsFromResourceOutput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_storage_gateway.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the resource that the tags were removed from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceOutput:
    out: RemoveTagsFromResourceOutput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    return out
