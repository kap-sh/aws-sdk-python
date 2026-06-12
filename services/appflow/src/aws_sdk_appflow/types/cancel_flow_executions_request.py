"""Generated from Smithy shape ``com.amazonaws.appflow#CancelFlowExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.execution_ids
    import aws_sdk_appflow.types.flow_name


class CancelFlowExecutionsRequest(TypedDict):
    flow_name: "aws_sdk_appflow.types.flow_name.FlowName"
    """<p>The name of a flow with active runs that you want to cancel.</p>"""
    execution_ids: NotRequired["aws_sdk_appflow.types.execution_ids.ExecutionIds"]
    """<p>The ID of each active run to cancel. These runs must belong to the flow you specify in your request.</p> <p>If you omit this parameter, your request ends all active runs that belong to the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelFlowExecutionsRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    if "execution_ids" in value:
        import aws_sdk_appflow.types.execution_ids

        out["executionIds"] = aws_sdk_appflow.types.execution_ids.serialize_json(
            value["execution_ids"]
        )
    return out


def deserialize_json(data: dict) -> CancelFlowExecutionsRequest:
    out: CancelFlowExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("CancelFlowExecutionsRequest.flow_name required")
    if "executionIds" in data:
        import aws_sdk_appflow.types.execution_ids

        out["execution_ids"] = aws_sdk_appflow.types.execution_ids.deserialize_json(
            data["executionIds"]
        )
    return out
