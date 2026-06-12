"""Generated from Smithy shape ``com.amazonaws.appflow#ListFlowsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.flow_list
    import aws_sdk_appflow.types.next_token


class ListFlowsResponse(TypedDict):
    flows: NotRequired["aws_sdk_appflow.types.flow_list.FlowList"]
    """<p> The list of flows associated with your account. </p>"""
    next_token: NotRequired["aws_sdk_appflow.types.next_token.NextToken"]
    """<p> The pagination token for next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowsResponse) -> dict:
    out: dict = {}
    if "flows" in value:
        import aws_sdk_appflow.types.flow_list

        out["flows"] = aws_sdk_appflow.types.flow_list.serialize_json(value["flows"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowsResponse:
    out: ListFlowsResponse = {}  # type: ignore[typeddict-item]
    if "flows" in data:
        import aws_sdk_appflow.types.flow_list

        out["flows"] = aws_sdk_appflow.types.flow_list.deserialize_json(data["flows"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
