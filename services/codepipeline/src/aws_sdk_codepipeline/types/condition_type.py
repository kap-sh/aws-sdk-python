"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ConditionType: TypeAlias = Literal[
    "BEFORE_ENTRY",
    "ON_SUCCESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEFORE_ENTRY",
        "ON_SUCCESS",
    )
)


def serialize_aws_json_1_1(value: ConditionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConditionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConditionType value: {data!r}")
    return cast(ConditionType, data)
