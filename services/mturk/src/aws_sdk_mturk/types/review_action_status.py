"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

ReviewActionStatus: TypeAlias = Literal[
    "Intended",
    "Succeeded",
    "Failed",
    "Cancelled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Intended",
        "Succeeded",
        "Failed",
        "Cancelled",
    )
)


def serialize_aws_json_1_1(value: ReviewActionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReviewActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReviewActionStatus value: {data!r}")
    return cast(ReviewActionStatus, data)
