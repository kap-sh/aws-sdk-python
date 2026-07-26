"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleCategory``."""

from typing import Literal, TypeAlias, cast

RuleCategory: TypeAlias = Literal["Rule",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleCategory:
    return cast(RuleCategory, data)
