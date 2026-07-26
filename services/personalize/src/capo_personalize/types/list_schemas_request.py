"""Generated from Smithy shape ``com.amazonaws.personalize#ListSchemasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.max_results
    import capo_personalize.types.next_token


class ListSchemasRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token returned from the previous call to <code>ListSchemas</code> for getting the next set of schemas (if they exist).</p>"""
    max_results: NotRequired["capo_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of schemas to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemasRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemasRequest:
    out: ListSchemasRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
