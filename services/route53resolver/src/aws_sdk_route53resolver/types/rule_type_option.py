"""Generated from Smithy shape ``com.amazonaws.route53resolver#RuleTypeOption``."""

from typing import Literal, TypeAlias, cast

RuleTypeOption: TypeAlias = Literal[
    "FORWARD",
    "SYSTEM",
    "RECURSIVE",
    "DELEGATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleTypeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleTypeOption:
    return cast(RuleTypeOption, data)
