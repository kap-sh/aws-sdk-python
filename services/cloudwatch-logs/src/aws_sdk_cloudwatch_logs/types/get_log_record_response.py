"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogRecordResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_record


class GetLogRecordResponse(TypedDict):
    log_record: NotRequired["aws_sdk_cloudwatch_logs.types.log_record.LogRecord"]
    """<p>The requested log event, as a JSON string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogRecordResponse) -> dict:
    out: dict = {}
    if "log_record" in value:
        import aws_sdk_cloudwatch_logs.types.log_record

        out["logRecord"] = (
            aws_sdk_cloudwatch_logs.types.log_record.serialize_aws_json_1_1(
                value["log_record"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogRecordResponse:
    out: GetLogRecordResponse = {}  # type: ignore[typeddict-item]
    if "logRecord" in data:
        import aws_sdk_cloudwatch_logs.types.log_record

        out["log_record"] = (
            aws_sdk_cloudwatch_logs.types.log_record.deserialize_aws_json_1_1(
                data["logRecord"]
            )
        )
    return out
