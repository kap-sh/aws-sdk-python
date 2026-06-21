"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyEffect``."""

from typing import Literal, TypeAlias, cast

PolicyEffect: TypeAlias = Literal[
    "Permit",
    "Forbid",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyEffect) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PolicyEffect:
    return cast(PolicyEffect, data)
