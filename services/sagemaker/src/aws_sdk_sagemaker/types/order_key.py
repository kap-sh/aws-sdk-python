"""Generated from Smithy shape ``com.amazonaws.sagemaker#OrderKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

OrderKey: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ascending",
        "Descending",
    )
)


def serialize_aws_json_1_1(value: OrderKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrderKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderKey value: {data!r}")
    return cast(OrderKey, data)
