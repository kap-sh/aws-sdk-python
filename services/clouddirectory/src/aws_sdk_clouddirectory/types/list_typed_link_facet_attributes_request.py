"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListTypedLinkFacetAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.number_results
    import aws_sdk_clouddirectory.types.typed_link_name


class ListTypedLinkFacetAttributesRequest(TypedDict, closed=True):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>"""
    name: "aws_sdk_clouddirectory.types.typed_link_name.TypedLinkName"
    """<p>The unique name of the typed link facet.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_clouddirectory.types.number_results.NumberResults"
    ]
    """<p>The maximum number of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTypedLinkFacetAttributesRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListTypedLinkFacetAttributesRequest:
    out: ListTypedLinkFacetAttributesRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ListTypedLinkFacetAttributesRequest.name required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
