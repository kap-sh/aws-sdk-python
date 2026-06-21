"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupPattern``."""

from typing import Literal, TypeAlias, cast

ProtectionGroupPattern: TypeAlias = Literal[
    "ALL",
    "ARBITRARY",
    "BY_RESOURCE_TYPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupPattern) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectionGroupPattern:
    return cast(ProtectionGroupPattern, data)
