"""Generated from Smithy shape ``com.amazonaws.ssm#SignalType``."""

from typing import Literal, TypeAlias, cast

SignalType: TypeAlias = Literal[
    "Approve",
    "Reject",
    "StartStep",
    "StopStep",
    "Resume",
    "Revoke",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignalType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SignalType:
    return cast(SignalType, data)
