"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmMuteRuleStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_status

AlarmMuteRuleStatuses: TypeAlias = list[
    "aws_sdk_cloudwatch.types.alarm_mute_rule_status.AlarmMuteRuleStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmMuteRuleStatuses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.alarm_mute_rule_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AlarmMuteRuleStatuses:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_status

    out: AlarmMuteRuleStatuses = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudwatch.types.alarm_mute_rule_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AlarmMuteRuleStatuses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.alarm_mute_rule_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AlarmMuteRuleStatuses:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_status

    out: AlarmMuteRuleStatuses = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudwatch.types.alarm_mute_rule_status.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmMuteRuleStatuses) -> list:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.alarm_mute_rule_status.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AlarmMuteRuleStatuses:
    import aws_sdk_cloudwatch.types.alarm_mute_rule_status

    out: AlarmMuteRuleStatuses = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.alarm_mute_rule_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
