"""Generated from Smithy shape ``com.amazonaws.servicequotas#AppliedLevelEnum``."""

from typing import Literal, TypeAlias, cast

AppliedLevelEnum: TypeAlias = Literal[
    "ACCOUNT",
    "RESOURCE",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppliedLevelEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppliedLevelEnum:
    return cast(AppliedLevelEnum, data)
