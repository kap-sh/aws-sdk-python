"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListPublishedSchemaArnsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results


class ListPublishedSchemaArnsRequest(TypedDict, closed=True):
    schema_arn: NotRequired["capo_clouddirectory.types.arn.Arn"]
    """<p>The response for <code>ListPublishedSchemaArns</code> when this parameter is used will list all minor version ARNs for a major version.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPublishedSchemaArnsRequest) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPublishedSchemaArnsRequest:
    out: ListPublishedSchemaArnsRequest = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
