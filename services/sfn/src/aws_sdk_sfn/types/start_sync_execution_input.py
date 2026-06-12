"""Generated from Smithy shape ``com.amazonaws.sfn#StartSyncExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.included_data
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.sensitive_data
    import aws_sdk_sfn.types.trace_header


class StartSyncExecutionInput(TypedDict):
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine to execute.</p>"""
    name: NotRequired["aws_sdk_sfn.types.name.Name"]
    """<p>The name of the execution.</p>"""
    input: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The string that contains the JSON input data for the execution, for example:</p> <p> <code>\"{\\"first_name\\" : \\"Alejandro\\"}\"</code> </p> <note> <p>If you don't include any JSON input data, you still must include the two braces, for example: <code>\"{}\"</code> </p> </note> <p>Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    trace_header: NotRequired["aws_sdk_sfn.types.trace_header.TraceHeader"]
    """<p>Passes the X-Ray trace header. The trace header can also be passed in the request payload.</p> <note> <p> For X-Ray traces, all Amazon Web Services services use the <code>X-Amzn-Trace-Id</code> header from the HTTP request. Using the header is the preferred mechanism to identify a trace. <code>StartExecution</code> and <code>StartSyncExecution</code> API operations can also use <code>traceHeader</code> from the body of the request payload. If <b>both</b> sources are provided, Step Functions will use the <b>header value</b> (preferred) over the value in the request body. </p> </note>"""
    included_data: NotRequired["aws_sdk_sfn.types.included_data.IncludedData"]
    """<p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call the API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartSyncExecutionInput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "input" in value:
        out["input"] = value["input"]
    if "trace_header" in value:
        out["traceHeader"] = value["trace_header"]
    if "included_data" in value:
        import aws_sdk_sfn.types.included_data

        out["includedData"] = aws_sdk_sfn.types.included_data.serialize_aws_json_1_0(
            value["included_data"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartSyncExecutionInput:
    out: StartSyncExecutionInput = {}  # type: ignore[typeddict-item]
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("StartSyncExecutionInput.state_machine_arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "input" in data:
        out["input"] = data["input"]
    if "traceHeader" in data:
        out["trace_header"] = data["traceHeader"]
    if "includedData" in data:
        import aws_sdk_sfn.types.included_data

        out["included_data"] = aws_sdk_sfn.types.included_data.deserialize_aws_json_1_0(
            data["includedData"]
        )
    return out
