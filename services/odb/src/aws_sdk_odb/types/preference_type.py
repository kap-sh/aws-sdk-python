"""Generated from Smithy shape ``com.amazonaws.odb#PreferenceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

PreferenceType: TypeAlias = Literal[
    "NO_PREFERENCE",
    "CUSTOM_PREFERENCE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PREFERENCE",
        "CUSTOM_PREFERENCE",
    )
)


def serialize_aws_json_1_0(value: PreferenceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PreferenceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreferenceType value: {data!r}")
    return cast(PreferenceType, data)
