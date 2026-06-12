"""Generated from Smithy shape ``com.amazonaws.kendra#MissingAttributeKeyStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

MissingAttributeKeyStrategy: TypeAlias = Literal[
    "IGNORE",
    "COLLAPSE",
    "EXPAND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE",
        "COLLAPSE",
        "EXPAND",
    )
)


def serialize_aws_json_1_1(value: MissingAttributeKeyStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MissingAttributeKeyStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MissingAttributeKeyStrategy value: {data!r}"
        )
    return cast(MissingAttributeKeyStrategy, data)
