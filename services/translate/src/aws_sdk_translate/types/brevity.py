"""Generated from Smithy shape ``com.amazonaws.translate#Brevity``."""

from typing import Literal, TypeAlias, cast

Brevity: TypeAlias = Literal["ON",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Brevity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Brevity:
    return cast(Brevity, data)
