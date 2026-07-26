"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetAlarmMuteRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.name


class GetAlarmMuteRuleInput(TypedDict, closed=True):
    alarm_mute_rule_name: NotRequired["capo_cloudwatch.types.name.Name"]
    """<p>The name of the alarm mute rule to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAlarmMuteRuleInput) -> dict:
    out: dict = {}
    if "alarm_mute_rule_name" in value:
        out["AlarmMuteRuleName"] = value["alarm_mute_rule_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAlarmMuteRuleInput:
    out: GetAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    if "AlarmMuteRuleName" in data:
        out["alarm_mute_rule_name"] = data["AlarmMuteRuleName"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAlarmMuteRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_mute_rule_name" in value:
        pairs.append(
            (f"{prefix}.AlarmMuteRuleName", str(value["alarm_mute_rule_name"]))
        )


def deserialize_query(el: Element) -> GetAlarmMuteRuleInput:
    out: GetAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    child_alarm_mute_rule_name = el.find("AlarmMuteRuleName")
    if child_alarm_mute_rule_name is not None:
        out["alarm_mute_rule_name"] = str(child_alarm_mute_rule_name.text or "")
    return out
