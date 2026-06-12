"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListFacetAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.facet_name
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.number_results


class ListFacetAttributesRequest(TypedDict):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the schema where the facet resides.</p>"""
    name: "aws_sdk_clouddirectory.types.facet_name.FacetName"
    """<p>The name of the facet whose attributes will be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_clouddirectory.types.number_results.NumberResults"
    ]
    """<p>The maximum number of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFacetAttributesRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListFacetAttributesRequest:
    out: ListFacetAttributesRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ListFacetAttributesRequest.name required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
