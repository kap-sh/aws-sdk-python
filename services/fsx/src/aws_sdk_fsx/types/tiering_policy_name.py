"""Generated from Smithy shape ``com.amazonaws.fsx#TieringPolicyName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

TieringPolicyName: TypeAlias = Literal[
    "SNAPSHOT_ONLY",
    "AUTO",
    "ALL",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SNAPSHOT_ONLY",
        "AUTO",
        "ALL",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: TieringPolicyName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TieringPolicyName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TieringPolicyName value: {data!r}")
    return cast(TieringPolicyName, data)
