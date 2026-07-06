"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListAlarmMuteRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_summaries
    import aws_sdk_cloudwatch.types.next_token


class ListAlarmMuteRulesOutput(TypedDict, closed=True):
    alarm_mute_rule_summaries: NotRequired[
        "aws_sdk_cloudwatch.types.alarm_mute_rule_summaries.AlarmMuteRuleSummaries"
    ]
    """<p>A list of alarm mute rule summaries.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of results. If this field is absent, there are no more results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAlarmMuteRulesOutput) -> dict:
    out: dict = {}
    if "alarm_mute_rule_summaries" in value:
        import aws_sdk_cloudwatch.types.alarm_mute_rule_summaries

        out["AlarmMuteRuleSummaries"] = (
            aws_sdk_cloudwatch.types.alarm_mute_rule_summaries.serialize_aws_json_1_0(
                value["alarm_mute_rule_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAlarmMuteRulesOutput:
    out: ListAlarmMuteRulesOutput = {}  # type: ignore[typeddict-item]
    if "AlarmMuteRuleSummaries" in data:
        import aws_sdk_cloudwatch.types.alarm_mute_rule_summaries

        out["alarm_mute_rule_summaries"] = (
            aws_sdk_cloudwatch.types.alarm_mute_rule_summaries.deserialize_aws_json_1_0(
                data["AlarmMuteRuleSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListAlarmMuteRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_mute_rule_summaries" in value:
        import aws_sdk_cloudwatch.types.alarm_mute_rule_summaries

        aws_sdk_cloudwatch.types.alarm_mute_rule_summaries.serialize_query(
            value["alarm_mute_rule_summaries"],
            pairs,
            f"{prefix}.AlarmMuteRuleSummaries",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListAlarmMuteRulesOutput:
    out: ListAlarmMuteRulesOutput = {}  # type: ignore[typeddict-item]
    child_alarm_mute_rule_summaries = el.find("AlarmMuteRuleSummaries")
    if child_alarm_mute_rule_summaries is not None:
        import aws_sdk_cloudwatch.types.alarm_mute_rule_summaries

        out["alarm_mute_rule_summaries"] = (
            aws_sdk_cloudwatch.types.alarm_mute_rule_summaries.deserialize_query(
                child_alarm_mute_rule_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
