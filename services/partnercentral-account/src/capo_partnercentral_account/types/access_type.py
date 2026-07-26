"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AccessType``."""

from typing import Literal, TypeAlias, cast

AccessType: TypeAlias = Literal[
    "ALLOW_ALL",
    "DENY_ALL",
    "ALLOW_BY_DEFAULT_DENY_SOME",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccessType:
    return cast(AccessType, data)
