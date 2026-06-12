"""Generated from Smithy shape ``com.amazonaws.transcribe#CLMLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

CLMLanguageCode: TypeAlias = Literal[
    "en-US",
    "hi-IN",
    "es-US",
    "en-GB",
    "en-AU",
    "de-DE",
    "ja-JP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "en-US",
        "hi-IN",
        "es-US",
        "en-GB",
        "en-AU",
        "de-DE",
        "ja-JP",
    )
)


def serialize_aws_json_1_1(value: CLMLanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CLMLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CLMLanguageCode value: {data!r}")
    return cast(CLMLanguageCode, data)
