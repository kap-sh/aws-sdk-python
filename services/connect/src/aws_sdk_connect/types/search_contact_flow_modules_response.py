"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactFlowModulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.contact_flow_module_search_summary_list
    import aws_sdk_connect.types.next_token2500


class SearchContactFlowModulesResponse(TypedDict, closed=True):
    contact_flow_modules: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_search_summary_list.ContactFlowModuleSearchSummaryList"
    ]
    """<p>The search criteria to be used to return flow modules.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of flows which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactFlowModulesResponse) -> dict:
    out: dict = {}
    if "contact_flow_modules" in value:
        import aws_sdk_connect.types.contact_flow_module_search_summary_list

        out["ContactFlowModules"] = (
            aws_sdk_connect.types.contact_flow_module_search_summary_list.serialize_json(
                value["contact_flow_modules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchContactFlowModulesResponse:
    out: SearchContactFlowModulesResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowModules" in data:
        import aws_sdk_connect.types.contact_flow_module_search_summary_list

        out["contact_flow_modules"] = (
            aws_sdk_connect.types.contact_flow_module_search_summary_list.deserialize_json(
                data["ContactFlowModules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
