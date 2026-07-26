"""Generated from Smithy shape ``com.amazonaws.waf#RuleUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.rule_update

RuleUpdates: TypeAlias = list["capo_waf.types.rule_update.RuleUpdate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleUpdates) -> list:
    import capo_waf.types.rule_update

    out: list = []
    for item in value:
        out.append(capo_waf.types.rule_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleUpdates:
    import capo_waf.types.rule_update

    out: RuleUpdates = []
    for item in data:
        out.append(capo_waf.types.rule_update.deserialize_aws_json_1_1(item))
    return out
