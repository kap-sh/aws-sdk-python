"""Generated from Smithy shape ``com.amazonaws.connectcases#ListTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.max_results
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.template_status_filters


class ListTemplatesRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    max_results: NotRequired["aws_sdk_connectcases.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    status: NotRequired[
        "aws_sdk_connectcases.types.template_status_filters.TemplateStatusFilters"
    ]
    """<p>A list of status values to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTemplatesRequest:
    out: ListTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
