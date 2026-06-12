"""Generated from Smithy shape ``com.amazonaws.comprehend#SyntaxLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

SyntaxLanguageCode: TypeAlias = Literal[
    "en",
    "es",
    "fr",
    "de",
    "it",
    "pt",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "en",
        "es",
        "fr",
        "de",
        "it",
        "pt",
    )
)


def serialize_aws_json_1_1(value: SyntaxLanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SyntaxLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SyntaxLanguageCode value: {data!r}")
    return cast(SyntaxLanguageCode, data)
