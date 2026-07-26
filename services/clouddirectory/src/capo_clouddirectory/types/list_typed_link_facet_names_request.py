"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListTypedLinkFacetNamesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results


class ListTypedLinkFacetNamesRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTypedLinkFacetNamesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListTypedLinkFacetNamesRequest:
    out: ListTypedLinkFacetNamesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
