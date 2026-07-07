"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListAlarmMuteRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_statuses
    import aws_sdk_cloudwatch.types.max_records
    import aws_sdk_cloudwatch.types.name
    import aws_sdk_cloudwatch.types.next_token


class ListAlarmMuteRulesInput(TypedDict, closed=True):
    alarm_name: NotRequired["aws_sdk_cloudwatch.types.name.Name"]
    """<p>Filter results to show only mute rules that target the specified alarm name.</p>"""
    statuses: NotRequired[
        "aws_sdk_cloudwatch.types.alarm_mute_rule_statuses.AlarmMuteRuleStatuses"
    ]
    """<p>Filter results to show only mute rules with the specified statuses. Valid values are <code>SCHEDULED</code>, <code>ACTIVE</code>, or <code>EXPIRED</code>.</p>"""
    max_records: NotRequired["aws_sdk_cloudwatch.types.max_records.MaxRecords"]
    """<p>The maximum number of mute rules to return in one call. The default is 50.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token returned from a previous call to indicate where to continue retrieving results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAlarmMuteRulesInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "statuses" in value:
        import aws_sdk_cloudwatch.types.alarm_mute_rule_statuses

        out["Statuses"] = (
            aws_sdk_cloudwatch.types.alarm_mute_rule_statuses.serialize_aws_json_1_0(
                value["statuses"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAlarmMuteRulesInput:
    out: ListAlarmMuteRulesInput = {}  # type: ignore[typeddict-item]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    if "Statuses" in data:
        import aws_sdk_cloudwatch.types.alarm_mute_rule_statuses

        out["statuses"] = (
            aws_sdk_cloudwatch.types.alarm_mute_rule_statuses.deserialize_aws_json_1_0(
                data["Statuses"]
            )
        )
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListAlarmMuteRulesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_name" in value:
        pairs.append((f"{prefix}.AlarmName", str(value["alarm_name"])))
    if "statuses" in value:
        import aws_sdk_cloudwatch.types.alarm_mute_rule_statuses

        aws_sdk_cloudwatch.types.alarm_mute_rule_statuses.serialize_query(
            value["statuses"], pairs, f"{prefix}.Statuses"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListAlarmMuteRulesInput:
    out: ListAlarmMuteRulesInput = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_statuses = el.find("Statuses")
    if child_statuses is not None:
        import aws_sdk_cloudwatch.types.alarm_mute_rule_statuses

        out["statuses"] = (
            aws_sdk_cloudwatch.types.alarm_mute_rule_statuses.deserialize_query(
                child_statuses
            )
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
