"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.taggable_resource_arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_mailmanager.types.taggable_resource_arn.TaggableResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to retrieve tags from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
