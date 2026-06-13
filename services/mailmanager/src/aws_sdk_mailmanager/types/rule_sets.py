"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_set

RuleSets: TypeAlias = list["aws_sdk_mailmanager.types.rule_set.RuleSet"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleSets) -> list:
    import aws_sdk_mailmanager.types.rule_set

    out: list = []
    for item in value:
        out.append(aws_sdk_mailmanager.types.rule_set.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RuleSets:
    import aws_sdk_mailmanager.types.rule_set

    out: RuleSets = []
    for item in data:
        out.append(aws_sdk_mailmanager.types.rule_set.deserialize_aws_json_1_0(item))
    return out
