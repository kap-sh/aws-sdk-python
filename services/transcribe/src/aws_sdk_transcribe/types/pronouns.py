"""Generated from Smithy shape ``com.amazonaws.transcribe#Pronouns``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

Pronouns: TypeAlias = Literal[
    "HE_HIM",
    "SHE_HER",
    "THEY_THEM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HE_HIM",
        "SHE_HER",
        "THEY_THEM",
    )
)


def serialize_aws_json_1_1(value: Pronouns) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Pronouns:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Pronouns value: {data!r}")
    return cast(Pronouns, data)
