"""Generated from Smithy shape ``com.amazonaws.codecommit#OrderEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

OrderEnum: TypeAlias = Literal[
    "ascending",
    "descending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ascending",
        "descending",
    )
)


def serialize_aws_json_1_1(value: OrderEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrderEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderEnum value: {data!r}")
    return cast(OrderEnum, data)
