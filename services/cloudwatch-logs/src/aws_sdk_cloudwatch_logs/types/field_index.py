"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FieldIndex``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.field_index_name
    import aws_sdk_cloudwatch_logs.types.index_type
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.timestamp


class FieldIndex(TypedDict):
    log_group_identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>If this field index appears in an index policy that applies only to a single log group, the ARN of that log group is displayed here.</p>"""
    field_index_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.field_index_name.FieldIndexName"
    ]
    """<p>The string that this field index matches.</p>"""
    last_scan_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The most recent time that CloudWatch Logs scanned ingested log events to search for this field index to improve the speed of future CloudWatch Logs Insights queries that search for this field index.</p>"""
    first_event_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time and date of the earliest log event that matches this field index, after the index policy that contains it was created. </p>"""
    last_event_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time and date of the most recent log event that matches this field index. </p>"""
    type: NotRequired["aws_sdk_cloudwatch_logs.types.index_type.IndexType"]
    """<p>The type of index. Specify <code>FACET</code> for facet-based indexing or <code>FIELD_INDEX</code> for field-based indexing. This determines how the field is indexed and can be queried.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldIndex) -> dict:
    out: dict = {}
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "field_index_name" in value:
        out["fieldIndexName"] = value["field_index_name"]
    if "last_scan_time" in value:
        out["lastScanTime"] = value["last_scan_time"]
    if "first_event_time" in value:
        out["firstEventTime"] = value["first_event_time"]
    if "last_event_time" in value:
        out["lastEventTime"] = value["last_event_time"]
    if "type" in value:
        import aws_sdk_cloudwatch_logs.types.index_type

        out["type"] = aws_sdk_cloudwatch_logs.types.index_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldIndex:
    out: FieldIndex = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if "fieldIndexName" in data:
        out["field_index_name"] = data["fieldIndexName"]
    if "lastScanTime" in data:
        out["last_scan_time"] = data["lastScanTime"]
    if "firstEventTime" in data:
        out["first_event_time"] = data["firstEventTime"]
    if "lastEventTime" in data:
        out["last_event_time"] = data["lastEventTime"]
    if "type" in data:
        import aws_sdk_cloudwatch_logs.types.index_type

        out["type"] = aws_sdk_cloudwatch_logs.types.index_type.deserialize_aws_json_1_1(
            data["type"]
        )
    return out
