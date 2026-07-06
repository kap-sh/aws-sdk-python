"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteAlarmMuteRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.name


class DeleteAlarmMuteRuleInput(TypedDict, closed=True):
    alarm_mute_rule_name: NotRequired["aws_sdk_cloudwatch.types.name.Name"]
    """<p>The name of the alarm mute rule to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAlarmMuteRuleInput) -> dict:
    out: dict = {}
    if "alarm_mute_rule_name" in value:
        out["AlarmMuteRuleName"] = value["alarm_mute_rule_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAlarmMuteRuleInput:
    out: DeleteAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    if "AlarmMuteRuleName" in data:
        out["alarm_mute_rule_name"] = data["AlarmMuteRuleName"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAlarmMuteRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_mute_rule_name" in value:
        pairs.append(
            (f"{prefix}.AlarmMuteRuleName", str(value["alarm_mute_rule_name"]))
        )


def deserialize_query(el: Element) -> DeleteAlarmMuteRuleInput:
    out: DeleteAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    child_alarm_mute_rule_name = el.find("AlarmMuteRuleName")
    if child_alarm_mute_rule_name is not None:
        out["alarm_mute_rule_name"] = str(child_alarm_mute_rule_name.text or "")
    return out
