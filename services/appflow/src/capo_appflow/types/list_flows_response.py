"""Generated from Smithy shape ``com.amazonaws.appflow#ListFlowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.flow_list
    import capo_appflow.types.next_token


class ListFlowsResponse(TypedDict, closed=True):
    flows: NotRequired["capo_appflow.types.flow_list.FlowList"]
    """<p> The list of flows associated with your account. </p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p> The pagination token for next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowsResponse) -> dict:
    out: dict = {}
    if "flows" in value:
        import capo_appflow.types.flow_list

        out["flows"] = capo_appflow.types.flow_list.serialize_json(value["flows"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowsResponse:
    out: ListFlowsResponse = {}  # type: ignore[typeddict-item]
    if "flows" in data:
        import capo_appflow.types.flow_list

        out["flows"] = capo_appflow.types.flow_list.deserialize_json(data["flows"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
