"""Generated from Smithy shape ``com.amazonaws.appflow#CancelFlowExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.execution_ids


class CancelFlowExecutionsResponse(TypedDict):
    invalid_executions: NotRequired["aws_sdk_appflow.types.execution_ids.ExecutionIds"]
    """<p>The IDs of runs that Amazon AppFlow couldn't cancel. These runs might be ineligible for canceling because they haven't started yet or have already completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelFlowExecutionsResponse) -> dict:
    out: dict = {}
    if "invalid_executions" in value:
        import aws_sdk_appflow.types.execution_ids

        out["invalidExecutions"] = aws_sdk_appflow.types.execution_ids.serialize_json(
            value["invalid_executions"]
        )
    return out


def deserialize_json(data: dict) -> CancelFlowExecutionsResponse:
    out: CancelFlowExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "invalidExecutions" in data:
        import aws_sdk_appflow.types.execution_ids

        out["invalid_executions"] = (
            aws_sdk_appflow.types.execution_ids.deserialize_json(
                data["invalidExecutions"]
            )
        )
    return out
