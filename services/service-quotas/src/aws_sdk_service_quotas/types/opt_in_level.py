"""Generated from Smithy shape ``com.amazonaws.servicequotas#OptInLevel``."""

from typing import Literal, TypeAlias, cast

OptInLevel: TypeAlias = Literal["ACCOUNT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptInLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptInLevel:
    return cast(OptInLevel, data)
