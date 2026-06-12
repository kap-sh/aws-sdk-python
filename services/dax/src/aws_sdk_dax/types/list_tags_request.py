"""Generated from Smithy shape ``com.amazonaws.dax#ListTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dax.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dax.types.string


class ListTagsRequest(TypedDict):
    resource_name: "aws_sdk_dax.types.string.String"
    """<p>The name of the DAX resource to which the tags belong.</p>"""
    next_token: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsRequest) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("ListTagsRequest.resource_name required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
