"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewPolicyLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

ReviewPolicyLevel: TypeAlias = Literal[
    "Assignment",
    "HIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Assignment",
        "HIT",
    )
)


def serialize_aws_json_1_1(value: ReviewPolicyLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReviewPolicyLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReviewPolicyLevel value: {data!r}")
    return cast(ReviewPolicyLevel, data)
