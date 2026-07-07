"""Generated from Smithy shape ``com.amazonaws.novaact#InvokeActStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.call_results
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name


class InvokeActStepRequest(TypedDict, closed=True):
    workflow_definition_name: (
        "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the act.</p>"""
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run containing the act.</p>"""
    session_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session containing the act.</p>"""
    act_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the act to invoke the next step for.</p>"""
    call_results: "aws_sdk_nova_act.types.call_results.CallResults"
    """<p>The results from previous tool calls that the act requested.</p>"""
    previous_step_id: NotRequired["aws_sdk_nova_act.types.uuid_string.UuidString"]
    """<p>The identifier of the previous step, used for tracking execution flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeActStepRequest) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.call_results

    out["callResults"] = aws_sdk_nova_act.types.call_results.serialize_json(
        value["call_results"]
    )
    if "previous_step_id" in value:
        out["previousStepId"] = value["previous_step_id"]
    return out


def deserialize_json(data: dict) -> InvokeActStepRequest:
    out: InvokeActStepRequest = {}  # type: ignore[typeddict-item]
    if "callResults" in data:
        import aws_sdk_nova_act.types.call_results

        out["call_results"] = aws_sdk_nova_act.types.call_results.deserialize_json(
            data["callResults"]
        )
    else:
        raise DeserializationError("InvokeActStepRequest.call_results required")
    if "previousStepId" in data:
        out["previous_step_id"] = data["previousStepId"]
    return out
