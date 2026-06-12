"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmHistoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_name
    import aws_sdk_cloudwatch.types.alarm_types
    import aws_sdk_cloudwatch.types.contributor_id
    import aws_sdk_cloudwatch.types.history_item_type
    import aws_sdk_cloudwatch.types.max_records
    import aws_sdk_cloudwatch.types.next_token
    import aws_sdk_cloudwatch.types.scan_by
    import aws_sdk_cloudwatch.types.timestamp


class DescribeAlarmHistoryInput(TypedDict):
    alarm_name: NotRequired["aws_sdk_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name of the alarm.</p>"""
    alarm_contributor_id: NotRequired[
        "aws_sdk_cloudwatch.types.contributor_id.ContributorId"
    ]
    """<p>The unique identifier of a specific alarm contributor to filter the alarm history results.</p>"""
    alarm_types: NotRequired["aws_sdk_cloudwatch.types.alarm_types.AlarmTypes"]
    """<p>Use this parameter to specify whether you want the operation to return metric alarms or composite alarms. If you omit this parameter, only metric alarms are returned.</p>"""
    history_item_type: NotRequired[
        "aws_sdk_cloudwatch.types.history_item_type.HistoryItemType"
    ]
    """<p>The type of alarm histories to retrieve.</p>"""
    start_date: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The starting date to retrieve alarm history.</p>"""
    end_date: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The ending date to retrieve alarm history.</p>"""
    max_records: NotRequired["aws_sdk_cloudwatch.types.max_records.MaxRecords"]
    """<p>The maximum number of alarm history records to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token returned by a previous call to indicate that there is more data available.</p>"""
    scan_by: NotRequired["aws_sdk_cloudwatch.types.scan_by.ScanBy"]
    """<p>Specified whether to return the newest or oldest alarm history first. Specify <code>TimestampDescending</code> to have the newest event history returned first, and specify <code>TimestampAscending</code> to have the oldest history returned first.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmHistoryInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_contributor_id" in value:
        out["AlarmContributorId"] = value["alarm_contributor_id"]
    if "alarm_types" in value:
        import aws_sdk_cloudwatch.types.alarm_types

        out["AlarmTypes"] = aws_sdk_cloudwatch.types.alarm_types.serialize_aws_json_1_0(
            value["alarm_types"]
        )
    if "history_item_type" in value:
        import aws_sdk_cloudwatch.types.history_item_type

        out["HistoryItemType"] = (
            aws_sdk_cloudwatch.types.history_item_type.serialize_aws_json_1_0(
                value["history_item_type"]
            )
        )
    if "start_date" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["StartDate"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["start_date"]
        )
    if "end_date" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["EndDate"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["end_date"]
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "scan_by" in value:
        import aws_sdk_cloudwatch.types.scan_by

        out["ScanBy"] = aws_sdk_cloudwatch.types.scan_by.serialize_aws_json_1_0(
            value["scan_by"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmHistoryInput:
    out: DescribeAlarmHistoryInput = {}  # type: ignore[typeddict-item]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    if "AlarmContributorId" in data:
        out["alarm_contributor_id"] = data["AlarmContributorId"]
    if "AlarmTypes" in data:
        import aws_sdk_cloudwatch.types.alarm_types

        out["alarm_types"] = (
            aws_sdk_cloudwatch.types.alarm_types.deserialize_aws_json_1_0(
                data["AlarmTypes"]
            )
        )
    if "HistoryItemType" in data:
        import aws_sdk_cloudwatch.types.history_item_type

        out["history_item_type"] = (
            aws_sdk_cloudwatch.types.history_item_type.deserialize_aws_json_1_0(
                data["HistoryItemType"]
            )
        )
    if "StartDate" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["start_date"] = aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["StartDate"]
        )
    if "EndDate" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["end_date"] = aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["EndDate"]
        )
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ScanBy" in data:
        import aws_sdk_cloudwatch.types.scan_by

        out["scan_by"] = aws_sdk_cloudwatch.types.scan_by.deserialize_aws_json_1_0(
            data["ScanBy"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmHistoryInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_name" in value:
        pairs.append((f"{prefix}.AlarmName", str(value["alarm_name"])))
    if "alarm_contributor_id" in value:
        pairs.append(
            (f"{prefix}.AlarmContributorId", str(value["alarm_contributor_id"]))
        )
    if "alarm_types" in value:
        import aws_sdk_cloudwatch.types.alarm_types

        aws_sdk_cloudwatch.types.alarm_types.serialize_query(
            value["alarm_types"], pairs, f"{prefix}.AlarmTypes"
        )
    if "history_item_type" in value:
        import aws_sdk_cloudwatch.types.history_item_type

        aws_sdk_cloudwatch.types.history_item_type.serialize_query(
            value["history_item_type"], pairs, f"{prefix}.HistoryItemType"
        )
    if "start_date" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["start_date"], pairs, f"{prefix}.StartDate"
        )
    if "end_date" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["end_date"], pairs, f"{prefix}.EndDate"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "scan_by" in value:
        import aws_sdk_cloudwatch.types.scan_by

        aws_sdk_cloudwatch.types.scan_by.serialize_query(
            value["scan_by"], pairs, f"{prefix}.ScanBy"
        )


def deserialize_query(el: Element) -> DescribeAlarmHistoryInput:
    out: DescribeAlarmHistoryInput = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_contributor_id = el.find("AlarmContributorId")
    if child_alarm_contributor_id is not None:
        out["alarm_contributor_id"] = str(child_alarm_contributor_id.text or "")
    child_alarm_types = el.find("AlarmTypes")
    if child_alarm_types is not None:
        import aws_sdk_cloudwatch.types.alarm_types

        out["alarm_types"] = aws_sdk_cloudwatch.types.alarm_types.deserialize_query(
            child_alarm_types
        )
    child_history_item_type = el.find("HistoryItemType")
    if child_history_item_type is not None:
        import aws_sdk_cloudwatch.types.history_item_type

        out["history_item_type"] = (
            aws_sdk_cloudwatch.types.history_item_type.deserialize_query(
                child_history_item_type
            )
        )
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["start_date"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_start_date
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["end_date"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_end_date
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_scan_by = el.find("ScanBy")
    if child_scan_by is not None:
        import aws_sdk_cloudwatch.types.scan_by

        out["scan_by"] = aws_sdk_cloudwatch.types.scan_by.deserialize_query(
            child_scan_by
        )
    return out
