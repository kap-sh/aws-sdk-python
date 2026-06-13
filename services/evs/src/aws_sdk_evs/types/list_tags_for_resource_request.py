"""Generated from Smithy shape ``com.amazonaws.evs#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_evs.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the resource to list tags for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
