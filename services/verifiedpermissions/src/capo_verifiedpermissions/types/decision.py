"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#Decision``."""

from typing import Literal, TypeAlias, cast

Decision: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Decision) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Decision:
    return cast(Decision, data)
