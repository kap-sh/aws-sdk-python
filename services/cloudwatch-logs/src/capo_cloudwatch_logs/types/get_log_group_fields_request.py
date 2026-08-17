"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogGroupFieldsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_identifier
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.timestamp


class GetLogGroupFieldsRequest(TypedDict, closed=True):
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group to search.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>"""
    time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time to set as the center of the query. If you specify <code>time</code>, the 8 minutes before and 8 minutes after this time are searched. If you omit <code>time</code>, the most recent 15 minutes up to the current time are searched.</p> <p>The <code>time</code> value is specified as epoch time, which is the number of seconds since <code>January 1, 1970, 00:00:00 UTC</code>.</p>"""
    log_group_identifier: NotRequired[
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>Specify either the name or ARN of the log group to view. If the log group is in a source account and you are using a monitoring account, you must specify the ARN.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogGroupFieldsRequest) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "time" in value:
        out["time"] = value["time"]
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogGroupFieldsRequest:
    out: GetLogGroupFieldsRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("time") is not None:
        out["time"] = data["time"]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    return out
