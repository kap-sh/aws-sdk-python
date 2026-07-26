"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListCommonControlsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.common_control_filter
    import capo_controlcatalog.types.max_list_common_controls_results
    import capo_controlcatalog.types.pagination_token


class ListCommonControlsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_controlcatalog.types.max_list_common_controls_results.MaxListCommonControlsResults"
    ]
    """<p>The maximum number of results on a page or for an API request call.</p>"""
    next_token: NotRequired[
        "capo_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    common_control_filter: NotRequired[
        "capo_controlcatalog.types.common_control_filter.CommonControlFilter"
    ]
    """<p>An optional filter that narrows the results to a specific objective.</p> <p>This filter allows you to specify one objective ARN at a time. Passing multiple ARNs in the <code>CommonControlFilter</code> isn’t supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommonControlsRequest) -> dict:
    out: dict = {}
    if "common_control_filter" in value:
        import capo_controlcatalog.types.common_control_filter

        out["CommonControlFilter"] = (
            capo_controlcatalog.types.common_control_filter.serialize_json(
                value["common_control_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCommonControlsRequest:
    out: ListCommonControlsRequest = {}  # type: ignore[typeddict-item]
    if "CommonControlFilter" in data:
        import capo_controlcatalog.types.common_control_filter

        out["common_control_filter"] = (
            capo_controlcatalog.types.common_control_filter.deserialize_json(
                data["CommonControlFilter"]
            )
        )
    return out
