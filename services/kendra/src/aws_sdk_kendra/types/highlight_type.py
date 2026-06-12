"""Generated from Smithy shape ``com.amazonaws.kendra#HighlightType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

HighlightType: TypeAlias = Literal[
    "STANDARD",
    "THESAURUS_SYNONYM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "THESAURUS_SYNONYM",
    )
)


def serialize_aws_json_1_1(value: HighlightType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HighlightType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HighlightType value: {data!r}")
    return cast(HighlightType, data)
