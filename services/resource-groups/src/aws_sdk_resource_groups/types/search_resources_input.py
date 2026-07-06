"""Generated from Smithy shape ``com.amazonaws.resourcegroups#SearchResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.max_results
    import aws_sdk_resource_groups.types.next_token
    import aws_sdk_resource_groups.types.resource_query


class SearchResourcesInput(TypedDict, closed=True):
    resource_query: "aws_sdk_resource_groups.types.resource_query.ResourceQuery"
    """<p>The search query, using the same formats that are supported for resource group definition. For more information, see <a>CreateGroup</a>.</p>"""
    max_results: NotRequired["aws_sdk_resource_groups.types.max_results.MaxResults"]
    """<p>The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    next_token: NotRequired["aws_sdk_resource_groups.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesInput) -> dict:
    out: dict = {}
    import aws_sdk_resource_groups.types.resource_query

    out["ResourceQuery"] = aws_sdk_resource_groups.types.resource_query.serialize_json(
        value["resource_query"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchResourcesInput:
    out: SearchResourcesInput = {}  # type: ignore[typeddict-item]
    if "ResourceQuery" in data:
        import aws_sdk_resource_groups.types.resource_query

        out["resource_query"] = (
            aws_sdk_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    else:
        raise DeserializationError("SearchResourcesInput.resource_query required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
