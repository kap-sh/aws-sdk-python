"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestStatusEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

PullRequestStatusEnum: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "CLOSED",
    )
)


def serialize_aws_json_1_1(value: PullRequestStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PullRequestStatusEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PullRequestStatusEnum value: {data!r}")
    return cast(PullRequestStatusEnum, data)
