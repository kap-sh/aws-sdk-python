"""Generated from Smithy shape ``com.amazonaws.xray#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.amazon_resource_name
    import aws_sdk_xray.types.string


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_xray.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Number (ARN) of an X-Ray group or sampling rule.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>A pagination token. If multiple pages of results are returned, use the <code>NextToken</code> value returned with the current page of results as the value of this parameter to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
