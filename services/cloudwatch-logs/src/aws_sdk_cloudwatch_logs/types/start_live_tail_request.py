"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTailRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.filter_pattern
    import aws_sdk_cloudwatch_logs.types.input_log_stream_names
    import aws_sdk_cloudwatch_logs.types.start_live_tail_log_group_identifiers


class StartLiveTailRequest(TypedDict):
    log_group_identifiers: "aws_sdk_cloudwatch_logs.types.start_live_tail_log_group_identifiers.StartLiveTailLogGroupIdentifiers"
    """<p>An array where each item in the array is a log group to include in the Live Tail session.</p> <p>Specify each log group by its ARN. </p> <p>If you specify an ARN, the ARN can't end with an asterisk (*).</p> <note> <p> You can include up to 10 log groups.</p> </note>"""
    log_stream_names: NotRequired[
        "aws_sdk_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
    ]
    """<p>If you specify this parameter, then only log events in the log streams that you specify here are included in the Live Tail session.</p> <p>If you specify this field, you can't also specify the <code>logStreamNamePrefixes</code> field.</p> <note> <p>You can specify this parameter only if you specify only one log group in <code>logGroupIdentifiers</code>.</p> </note>"""
    log_stream_name_prefixes: NotRequired[
        "aws_sdk_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
    ]
    """<p>If you specify this parameter, then only log events in the log streams that have names that start with the prefixes that you specify here are included in the Live Tail session.</p> <p>If you specify this field, you can't also specify the <code>logStreamNames</code> field.</p> <note> <p>You can specify this parameter only if you specify only one log group in <code>logGroupIdentifiers</code>.</p> </note>"""
    log_event_filter_pattern: NotRequired[
        "aws_sdk_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    """<p>An optional pattern to use to filter the results to include only log events that match the pattern. For example, a filter pattern of <code>error 404</code> causes only log events that include both <code>error</code> and <code>404</code> to be included in the Live Tail stream.</p> <p>Regular expression filter patterns are supported.</p> <p>For more information about filter pattern syntax, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html\">Filter and Pattern Syntax</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLiveTailRequest) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.start_live_tail_log_group_identifiers

    out["logGroupIdentifiers"] = (
        aws_sdk_cloudwatch_logs.types.start_live_tail_log_group_identifiers.serialize_aws_json_1_1(
            value["log_group_identifiers"]
        )
    )
    if "log_stream_names" in value:
        import aws_sdk_cloudwatch_logs.types.input_log_stream_names

        out["logStreamNames"] = (
            aws_sdk_cloudwatch_logs.types.input_log_stream_names.serialize_aws_json_1_1(
                value["log_stream_names"]
            )
        )
    if "log_stream_name_prefixes" in value:
        import aws_sdk_cloudwatch_logs.types.input_log_stream_names

        out["logStreamNamePrefixes"] = (
            aws_sdk_cloudwatch_logs.types.input_log_stream_names.serialize_aws_json_1_1(
                value["log_stream_name_prefixes"]
            )
        )
    if "log_event_filter_pattern" in value:
        out["logEventFilterPattern"] = value["log_event_filter_pattern"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLiveTailRequest:
    out: StartLiveTailRequest = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.start_live_tail_log_group_identifiers

        out["log_group_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.start_live_tail_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "StartLiveTailRequest.log_group_identifiers required"
        )
    if "logStreamNames" in data:
        import aws_sdk_cloudwatch_logs.types.input_log_stream_names

        out["log_stream_names"] = (
            aws_sdk_cloudwatch_logs.types.input_log_stream_names.deserialize_aws_json_1_1(
                data["logStreamNames"]
            )
        )
    if "logStreamNamePrefixes" in data:
        import aws_sdk_cloudwatch_logs.types.input_log_stream_names

        out["log_stream_name_prefixes"] = (
            aws_sdk_cloudwatch_logs.types.input_log_stream_names.deserialize_aws_json_1_1(
                data["logStreamNamePrefixes"]
            )
        )
    if "logEventFilterPattern" in data:
        out["log_event_filter_pattern"] = data["logEventFilterPattern"]
    return out
