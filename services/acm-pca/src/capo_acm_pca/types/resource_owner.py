"""Generated from Smithy shape ``com.amazonaws.acmpca#ResourceOwner``."""

from typing import Literal, TypeAlias, cast

ResourceOwner: TypeAlias = Literal[
    "SELF",
    "OTHER_ACCOUNTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceOwner) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceOwner:
    return cast(ResourceOwner, data)
