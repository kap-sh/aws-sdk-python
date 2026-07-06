"""Generated from Smithy shape ``com.amazonaws.kendraranking#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_kendra_ranking.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the rescore execution plan to get a list of tags for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
