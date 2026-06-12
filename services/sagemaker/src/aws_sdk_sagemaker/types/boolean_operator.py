"""Generated from Smithy shape ``com.amazonaws.sagemaker#BooleanOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

BooleanOperator: TypeAlias = Literal[
    "And",
    "Or",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "And",
        "Or",
    )
)


def serialize_aws_json_1_1(value: BooleanOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BooleanOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BooleanOperator value: {data!r}")
    return cast(BooleanOperator, data)
