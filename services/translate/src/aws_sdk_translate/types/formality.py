"""Generated from Smithy shape ``com.amazonaws.translate#Formality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

Formality: TypeAlias = Literal[
    "FORMAL",
    "INFORMAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FORMAL",
        "INFORMAL",
    )
)


def serialize_aws_json_1_1(value: Formality) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Formality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Formality value: {data!r}")
    return cast(Formality, data)
