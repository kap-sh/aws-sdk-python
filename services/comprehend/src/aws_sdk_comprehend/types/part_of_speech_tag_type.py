"""Generated from Smithy shape ``com.amazonaws.comprehend#PartOfSpeechTagType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

PartOfSpeechTagType: TypeAlias = Literal[
    "ADJ",
    "ADP",
    "ADV",
    "AUX",
    "CONJ",
    "CCONJ",
    "DET",
    "INTJ",
    "NOUN",
    "NUM",
    "O",
    "PART",
    "PRON",
    "PROPN",
    "PUNCT",
    "SCONJ",
    "SYM",
    "VERB",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADJ",
        "ADP",
        "ADV",
        "AUX",
        "CONJ",
        "CCONJ",
        "DET",
        "INTJ",
        "NOUN",
        "NUM",
        "O",
        "PART",
        "PRON",
        "PROPN",
        "PUNCT",
        "SCONJ",
        "SYM",
        "VERB",
    )
)


def serialize_aws_json_1_1(value: PartOfSpeechTagType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartOfSpeechTagType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartOfSpeechTagType value: {data!r}")
    return cast(PartOfSpeechTagType, data)
