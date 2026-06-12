"""Generated from Smithy shape ``com.amazonaws.ecr#SigningRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.signing_rule

SigningRuleList: TypeAlias = list["aws_sdk_ecr.types.signing_rule.SigningRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningRuleList) -> list:
    import aws_sdk_ecr.types.signing_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.signing_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SigningRuleList:
    import aws_sdk_ecr.types.signing_rule

    out: SigningRuleList = []
    for item in data:
        out.append(aws_sdk_ecr.types.signing_rule.deserialize_aws_json_1_1(item))
    return out
