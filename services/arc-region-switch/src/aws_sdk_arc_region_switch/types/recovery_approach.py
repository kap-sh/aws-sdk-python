"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RecoveryApproach``."""

from typing import Literal, TypeAlias, cast

RecoveryApproach: TypeAlias = Literal[
    "activeActive",
    "activePassive",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecoveryApproach) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecoveryApproach:
    return cast(RecoveryApproach, data)
