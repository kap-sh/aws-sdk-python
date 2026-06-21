"""Generated from Smithy shape ``com.amazonaws.wafv2#DataProtectionAction``."""

from typing import Literal, TypeAlias, cast

DataProtectionAction: TypeAlias = Literal[
    "SUBSTITUTION",
    "HASH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProtectionAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataProtectionAction:
    return cast(DataProtectionAction, data)
