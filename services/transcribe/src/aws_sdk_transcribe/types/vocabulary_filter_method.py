"""Generated from Smithy shape ``com.amazonaws.transcribe#VocabularyFilterMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

VocabularyFilterMethod: TypeAlias = Literal[
    "remove",
    "mask",
    "tag",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "remove",
        "mask",
        "tag",
    )
)


def serialize_aws_json_1_1(value: VocabularyFilterMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VocabularyFilterMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VocabularyFilterMethod value: {data!r}")
    return cast(VocabularyFilterMethod, data)
