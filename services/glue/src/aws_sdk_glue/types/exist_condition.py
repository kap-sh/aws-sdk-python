"""Generated from Smithy shape ``com.amazonaws.glue#ExistCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ExistCondition: TypeAlias = Literal[
    "MUST_EXIST",
    "NOT_EXIST",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MUST_EXIST",
        "NOT_EXIST",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: ExistCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExistCondition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExistCondition value: {data!r}")
    return cast(ExistCondition, data)
