"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleDmarcValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_dmarc_policy

RuleDmarcValueList: TypeAlias = list[
    "aws_sdk_mailmanager.types.rule_dmarc_policy.RuleDmarcPolicy"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleDmarcValueList) -> list:
    import aws_sdk_mailmanager.types.rule_dmarc_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mailmanager.types.rule_dmarc_policy.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RuleDmarcValueList:
    import aws_sdk_mailmanager.types.rule_dmarc_policy

    out: RuleDmarcValueList = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.rule_dmarc_policy.deserialize_aws_json_1_0(item)
        )
    return out
