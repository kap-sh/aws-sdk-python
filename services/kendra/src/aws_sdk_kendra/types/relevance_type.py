"""Generated from Smithy shape ``com.amazonaws.kendra#RelevanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

RelevanceType: TypeAlias = Literal[
    "RELEVANT",
    "NOT_RELEVANT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RELEVANT",
        "NOT_RELEVANT",
    )
)


def serialize_aws_json_1_1(value: RelevanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelevanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelevanceType value: {data!r}")
    return cast(RelevanceType, data)
