"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_verdict

RuleVerdictValueList: TypeAlias = list[
    "aws_sdk_mailmanager.types.rule_verdict.RuleVerdict"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdictValueList) -> list:
    import aws_sdk_mailmanager.types.rule_verdict

    out: list = []
    for item in value:
        out.append(aws_sdk_mailmanager.types.rule_verdict.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RuleVerdictValueList:
    import aws_sdk_mailmanager.types.rule_verdict

    out: RuleVerdictValueList = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.rule_verdict.deserialize_aws_json_1_0(item)
        )
    return out
