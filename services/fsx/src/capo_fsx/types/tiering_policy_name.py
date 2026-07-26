"""Generated from Smithy shape ``com.amazonaws.fsx#TieringPolicyName``."""

from typing import Literal, TypeAlias, cast

TieringPolicyName: TypeAlias = Literal[
    "SNAPSHOT_ONLY",
    "AUTO",
    "ALL",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TieringPolicyName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TieringPolicyName:
    return cast(TieringPolicyName, data)
