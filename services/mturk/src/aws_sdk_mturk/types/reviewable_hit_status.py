"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewableHITStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

ReviewableHITStatus: TypeAlias = Literal[
    "Reviewable",
    "Reviewing",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Reviewable",
        "Reviewing",
    )
)


def serialize_aws_json_1_1(value: ReviewableHITStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReviewableHITStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReviewableHITStatus value: {data!r}")
    return cast(ReviewableHITStatus, data)
