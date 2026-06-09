"""Generated from Smithy shape ``com.amazonaws.kms#IncludeKeyMaterial``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

IncludeKeyMaterial: TypeAlias = Literal[
    "ALL_KEY_MATERIAL",
    "ROTATIONS_ONLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_KEY_MATERIAL",
        "ROTATIONS_ONLY",
    )
)


def serialize_aws_json_1_1(value: IncludeKeyMaterial) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IncludeKeyMaterial:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludeKeyMaterial value: {data!r}")
    return cast(IncludeKeyMaterial, data)
