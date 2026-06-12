"""Generated from Smithy shape ``com.amazonaws.comprehend#ToxicContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

ToxicContentType: TypeAlias = Literal[
    "GRAPHIC",
    "HARASSMENT_OR_ABUSE",
    "HATE_SPEECH",
    "INSULT",
    "PROFANITY",
    "SEXUAL",
    "VIOLENCE_OR_THREAT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GRAPHIC",
        "HARASSMENT_OR_ABUSE",
        "HATE_SPEECH",
        "INSULT",
        "PROFANITY",
        "SEXUAL",
        "VIOLENCE_OR_THREAT",
    )
)


def serialize_aws_json_1_1(value: ToxicContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ToxicContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ToxicContentType value: {data!r}")
    return cast(ToxicContentType, data)
