"""Generated from Smithy shape ``com.amazonaws.sfn#StartSyncExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.billing_details
    import aws_sdk_sfn.types.cloud_watch_events_execution_data_details
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.sensitive_cause
    import aws_sdk_sfn.types.sensitive_data
    import aws_sdk_sfn.types.sensitive_error
    import aws_sdk_sfn.types.sync_execution_status
    import aws_sdk_sfn.types.timestamp
    import aws_sdk_sfn.types.trace_header


class StartSyncExecutionOutput(TypedDict, closed=True):
    execution_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the execution.</p>"""
    state_machine_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies the state machine.</p>"""
    name: NotRequired["aws_sdk_sfn.types.name.Name"]
    """<p>The name of the execution.</p>"""
    start_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the execution is started.</p>"""
    stop_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>If the execution has already ended, the date the execution stopped.</p>"""
    status: "aws_sdk_sfn.types.sync_execution_status.SyncExecutionStatus"
    """<p>The current status of the execution.</p>"""
    error: NotRequired["aws_sdk_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error code of the failure.</p>"""
    cause: NotRequired["aws_sdk_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A more detailed explanation of the cause of the failure.</p>"""
    input: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The string that contains the JSON input data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    input_details: NotRequired[
        "aws_sdk_sfn.types.cloud_watch_events_execution_data_details.CloudWatchEventsExecutionDataDetails"
    ]
    output: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON output data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p> <note> <p>This field is set only if the execution succeeds. If the execution fails, this field is null.</p> </note>"""
    output_details: NotRequired[
        "aws_sdk_sfn.types.cloud_watch_events_execution_data_details.CloudWatchEventsExecutionDataDetails"
    ]
    trace_header: NotRequired["aws_sdk_sfn.types.trace_header.TraceHeader"]
    """<p>The X-Ray trace header that was passed to the execution.</p> <note> <p> For X-Ray traces, all Amazon Web Services services use the <code>X-Amzn-Trace-Id</code> header from the HTTP request. Using the header is the preferred mechanism to identify a trace. <code>StartExecution</code> and <code>StartSyncExecution</code> API operations can also use <code>traceHeader</code> from the body of the request payload. If <b>both</b> sources are provided, Step Functions will use the <b>header value</b> (preferred) over the value in the request body. </p> </note>"""
    billing_details: NotRequired["aws_sdk_sfn.types.billing_details.BillingDetails"]
    """<p>An object that describes workflow billing details, including billed duration and memory use.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartSyncExecutionOutput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    if "state_machine_arn" in value:
        out["stateMachineArn"] = value["state_machine_arn"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_sfn.types.timestamp

    out["startDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    import aws_sdk_sfn.types.timestamp

    out["stopDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["stop_date"]
    )
    import aws_sdk_sfn.types.sync_execution_status

    out["status"] = aws_sdk_sfn.types.sync_execution_status.serialize_aws_json_1_0(
        value["status"]
    )
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    if "input" in value:
        out["input"] = value["input"]
    if "input_details" in value:
        import aws_sdk_sfn.types.cloud_watch_events_execution_data_details

        out["inputDetails"] = (
            aws_sdk_sfn.types.cloud_watch_events_execution_data_details.serialize_aws_json_1_0(
                value["input_details"]
            )
        )
    if "output" in value:
        out["output"] = value["output"]
    if "output_details" in value:
        import aws_sdk_sfn.types.cloud_watch_events_execution_data_details

        out["outputDetails"] = (
            aws_sdk_sfn.types.cloud_watch_events_execution_data_details.serialize_aws_json_1_0(
                value["output_details"]
            )
        )
    if "trace_header" in value:
        out["traceHeader"] = value["trace_header"]
    if "billing_details" in value:
        import aws_sdk_sfn.types.billing_details

        out["billingDetails"] = (
            aws_sdk_sfn.types.billing_details.serialize_aws_json_1_0(
                value["billing_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartSyncExecutionOutput:
    out: StartSyncExecutionOutput = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("StartSyncExecutionOutput.execution_arn required")
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "startDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["start_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        raise DeserializationError("StartSyncExecutionOutput.start_date required")
    if "stopDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["stop_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    else:
        raise DeserializationError("StartSyncExecutionOutput.stop_date required")
    if "status" in data:
        import aws_sdk_sfn.types.sync_execution_status

        out["status"] = (
            aws_sdk_sfn.types.sync_execution_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StartSyncExecutionOutput.status required")
    if "error" in data:
        out["error"] = data["error"]
    if "cause" in data:
        out["cause"] = data["cause"]
    if "input" in data:
        out["input"] = data["input"]
    if "inputDetails" in data:
        import aws_sdk_sfn.types.cloud_watch_events_execution_data_details

        out["input_details"] = (
            aws_sdk_sfn.types.cloud_watch_events_execution_data_details.deserialize_aws_json_1_0(
                data["inputDetails"]
            )
        )
    if "output" in data:
        out["output"] = data["output"]
    if "outputDetails" in data:
        import aws_sdk_sfn.types.cloud_watch_events_execution_data_details

        out["output_details"] = (
            aws_sdk_sfn.types.cloud_watch_events_execution_data_details.deserialize_aws_json_1_0(
                data["outputDetails"]
            )
        )
    if "traceHeader" in data:
        out["trace_header"] = data["traceHeader"]
    if "billingDetails" in data:
        import aws_sdk_sfn.types.billing_details

        out["billing_details"] = (
            aws_sdk_sfn.types.billing_details.deserialize_aws_json_1_0(
                data["billingDetails"]
            )
        )
    return out
