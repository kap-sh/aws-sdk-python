"""Generated from Smithy shape ``com.amazonaws.odb#PreferenceType``."""

from typing import Literal, TypeAlias, cast

PreferenceType: TypeAlias = Literal[
    "NO_PREFERENCE",
    "CUSTOM_PREFERENCE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferenceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PreferenceType:
    return cast(PreferenceType, data)
