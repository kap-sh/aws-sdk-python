"""Generated from Smithy shape ``com.amazonaws.datapipeline#OperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_data_pipeline.errors import DeserializationError

OperatorType: TypeAlias = Literal[
    "EQ",
    "REF_EQ",
    "LE",
    "GE",
    "BETWEEN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "REF_EQ",
        "LE",
        "GE",
        "BETWEEN",
    )
)


def serialize_aws_json_1_1(value: OperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperatorType value: {data!r}")
    return cast(OperatorType, data)
