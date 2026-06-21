"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleOwner``."""

from typing import Literal, TypeAlias, cast

RuleOwner: TypeAlias = Literal["AWS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleOwner) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleOwner:
    return cast(RuleOwner, data)
