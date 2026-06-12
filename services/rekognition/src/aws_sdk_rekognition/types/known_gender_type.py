"""Generated from Smithy shape ``com.amazonaws.rekognition#KnownGenderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

"""<p>A list of enum string of possible gender values that Celebrity returns.</p>"""
KnownGenderType: TypeAlias = Literal[
    "Male",
    "Female",
    "Nonbinary",
    "Unlisted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Male",
        "Female",
        "Nonbinary",
        "Unlisted",
    )
)


def serialize_aws_json_1_1(value: KnownGenderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KnownGenderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KnownGenderType value: {data!r}")
    return cast(KnownGenderType, data)
