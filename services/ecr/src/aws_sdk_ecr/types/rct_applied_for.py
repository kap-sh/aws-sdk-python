"""Generated from Smithy shape ``com.amazonaws.ecr#RCTAppliedFor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

RCTAppliedFor: TypeAlias = Literal[
    "REPLICATION",
    "PULL_THROUGH_CACHE",
    "CREATE_ON_PUSH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REPLICATION",
        "PULL_THROUGH_CACHE",
        "CREATE_ON_PUSH",
    )
)


def serialize_aws_json_1_1(value: RCTAppliedFor) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RCTAppliedFor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RCTAppliedFor value: {data!r}")
    return cast(RCTAppliedFor, data)
