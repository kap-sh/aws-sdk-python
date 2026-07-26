"""Generated from Smithy shape ``com.amazonaws.connect#ListFlowAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.flow_association_summary_list
    import capo_connect.types.next_token


class ListFlowAssociationsResponse(TypedDict, closed=True):
    flow_association_summary_list: NotRequired[
        "capo_connect.types.flow_association_summary_list.FlowAssociationSummaryList"
    ]
    """<p>Summary of flow associations.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowAssociationsResponse) -> dict:
    out: dict = {}
    if "flow_association_summary_list" in value:
        import capo_connect.types.flow_association_summary_list

        out["FlowAssociationSummaryList"] = (
            capo_connect.types.flow_association_summary_list.serialize_json(
                value["flow_association_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowAssociationsResponse:
    out: ListFlowAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "FlowAssociationSummaryList" in data:
        import capo_connect.types.flow_association_summary_list

        out["flow_association_summary_list"] = (
            capo_connect.types.flow_association_summary_list.deserialize_json(
                data["FlowAssociationSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
