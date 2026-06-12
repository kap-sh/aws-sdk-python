"""Generated from Smithy shape ``com.amazonaws.connect#ListFlowAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.flow_association_summary_list
    import aws_sdk_connect.types.next_token


class ListFlowAssociationsResponse(TypedDict):
    flow_association_summary_list: NotRequired[
        "aws_sdk_connect.types.flow_association_summary_list.FlowAssociationSummaryList"
    ]
    """<p>Summary of flow associations.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowAssociationsResponse) -> dict:
    out: dict = {}
    if "flow_association_summary_list" in value:
        import aws_sdk_connect.types.flow_association_summary_list

        out["FlowAssociationSummaryList"] = (
            aws_sdk_connect.types.flow_association_summary_list.serialize_json(
                value["flow_association_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowAssociationsResponse:
    out: ListFlowAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "FlowAssociationSummaryList" in data:
        import aws_sdk_connect.types.flow_association_summary_list

        out["flow_association_summary_list"] = (
            aws_sdk_connect.types.flow_association_summary_list.deserialize_json(
                data["FlowAssociationSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
