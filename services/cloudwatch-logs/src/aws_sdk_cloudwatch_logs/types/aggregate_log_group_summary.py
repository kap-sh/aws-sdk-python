"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AggregateLogGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.grouping_identifiers
    import aws_sdk_cloudwatch_logs.types.log_group_count


class AggregateLogGroupSummary(TypedDict, closed=True):
    log_group_count: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_count.LogGroupCount"
    ]
    """<p>The number of log groups in this aggregate summary group.</p>"""
    grouping_identifiers: NotRequired[
        "aws_sdk_cloudwatch_logs.types.grouping_identifiers.GroupingIdentifiers"
    ]
    """<p>An array of key-value pairs that identify the data source characteristics used to group the log groups.</p> <p>The size and content of this array depends on the <code>groupBy</code> parameter specified in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateLogGroupSummary) -> dict:
    out: dict = {}
    if "log_group_count" in value:
        out["logGroupCount"] = value["log_group_count"]
    if "grouping_identifiers" in value:
        import aws_sdk_cloudwatch_logs.types.grouping_identifiers

        out["groupingIdentifiers"] = (
            aws_sdk_cloudwatch_logs.types.grouping_identifiers.serialize_aws_json_1_1(
                value["grouping_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateLogGroupSummary:
    out: AggregateLogGroupSummary = {}  # type: ignore[typeddict-item]
    if "logGroupCount" in data:
        out["log_group_count"] = data["logGroupCount"]
    if "groupingIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.grouping_identifiers

        out["grouping_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.grouping_identifiers.deserialize_aws_json_1_1(
                data["groupingIdentifiers"]
            )
        )
    return out
