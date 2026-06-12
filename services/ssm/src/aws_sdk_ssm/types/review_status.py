"""Generated from Smithy shape ``com.amazonaws.ssm#ReviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ReviewStatus: TypeAlias = Literal[
    "APPROVED",
    "NOT_REVIEWED",
    "PENDING",
    "REJECTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVED",
        "NOT_REVIEWED",
        "PENDING",
        "REJECTED",
    )
)


def serialize_aws_json_1_1(value: ReviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReviewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReviewStatus value: {data!r}")
    return cast(ReviewStatus, data)
