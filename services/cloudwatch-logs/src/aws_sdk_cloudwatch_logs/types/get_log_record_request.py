"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogRecordRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_record_pointer
    import aws_sdk_cloudwatch_logs.types.unmask


class GetLogRecordRequest(TypedDict):
    log_record_pointer: (
        "aws_sdk_cloudwatch_logs.types.log_record_pointer.LogRecordPointer"
    )
    """<p>The pointer corresponding to the log event record you want to retrieve. You get this from the response of a <code>GetQueryResults</code> operation. In that response, the value of the <code>@ptr</code> field for a log event is the value to use as <code>logRecordPointer</code> to retrieve that complete log event record.</p>"""
    unmask: "aws_sdk_cloudwatch_logs.types.unmask.Unmask"
    """<p>Specify <code>true</code> to display the log event fields with all sensitive data unmasked and visible. The default is <code>false</code>.</p> <p>To use this operation with this parameter, you must be signed into an account with the <code>logs:Unmask</code> permission.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogRecordRequest) -> dict:
    out: dict = {}
    out["logRecordPointer"] = value["log_record_pointer"]
    out["unmask"] = value.get("unmask", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogRecordRequest:
    out: GetLogRecordRequest = {}  # type: ignore[typeddict-item]
    if "logRecordPointer" in data:
        out["log_record_pointer"] = data["logRecordPointer"]
    else:
        raise DeserializationError("GetLogRecordRequest.log_record_pointer required")
    if "unmask" in data:
        out["unmask"] = data["unmask"]
    else:
        out["unmask"] = False
    return out
