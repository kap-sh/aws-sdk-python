"""Generated from Smithy shape ``com.amazonaws.sfn#TestStateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sfn.types.inspection_data
    import aws_sdk_sfn.types.sensitive_cause
    import aws_sdk_sfn.types.sensitive_data
    import aws_sdk_sfn.types.sensitive_error
    import aws_sdk_sfn.types.state_name
    import aws_sdk_sfn.types.test_execution_status


class TestStateOutput(TypedDict, closed=True):
    output: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON output data of the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    error: NotRequired["aws_sdk_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error returned when the execution of a state fails.</p>"""
    cause: NotRequired["aws_sdk_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A detailed explanation of the cause for the error when the execution of a state fails.</p>"""
    inspection_data: NotRequired["aws_sdk_sfn.types.inspection_data.InspectionData"]
    """<p>Returns additional details about the state's execution, including its input and output data processing flow, and HTTP request and response information. The <code>inspectionLevel</code> request parameter specifies which details are returned.</p>"""
    next_state: NotRequired["aws_sdk_sfn.types.state_name.StateName"]
    """<p>The name of the next state to transition to. If you haven't defined a next state in your definition or if the execution of the state fails, this field doesn't contain a value.</p>"""
    status: NotRequired["aws_sdk_sfn.types.test_execution_status.TestExecutionStatus"]
    """<p>The execution status of the state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestStateOutput) -> dict:
    out: dict = {}
    if "output" in value:
        out["output"] = value["output"]
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    if "inspection_data" in value:
        import aws_sdk_sfn.types.inspection_data

        out["inspectionData"] = (
            aws_sdk_sfn.types.inspection_data.serialize_aws_json_1_0(
                value["inspection_data"]
            )
        )
    if "next_state" in value:
        out["nextState"] = value["next_state"]
    if "status" in value:
        import aws_sdk_sfn.types.test_execution_status

        out["status"] = aws_sdk_sfn.types.test_execution_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestStateOutput:
    out: TestStateOutput = {}  # type: ignore[typeddict-item]
    if "output" in data:
        out["output"] = data["output"]
    if "error" in data:
        out["error"] = data["error"]
    if "cause" in data:
        out["cause"] = data["cause"]
    if "inspectionData" in data:
        import aws_sdk_sfn.types.inspection_data

        out["inspection_data"] = (
            aws_sdk_sfn.types.inspection_data.deserialize_aws_json_1_0(
                data["inspectionData"]
            )
        )
    if "nextState" in data:
        out["next_state"] = data["nextState"]
    if "status" in data:
        import aws_sdk_sfn.types.test_execution_status

        out["status"] = (
            aws_sdk_sfn.types.test_execution_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
