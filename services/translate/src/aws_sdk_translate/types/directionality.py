"""Generated from Smithy shape ``com.amazonaws.translate#Directionality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

Directionality: TypeAlias = Literal[
    "UNI",
    "MULTI",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNI",
        "MULTI",
    )
)


def serialize_aws_json_1_1(value: Directionality) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Directionality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Directionality value: {data!r}")
    return cast(Directionality, data)
