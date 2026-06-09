"""Generated from Smithy shape ``com.amazonaws.kms#ImportType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

ImportType: TypeAlias = Literal[
    "NEW_KEY_MATERIAL",
    "EXISTING_KEY_MATERIAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW_KEY_MATERIAL",
        "EXISTING_KEY_MATERIAL",
    )
)


def serialize_aws_json_1_1(value: ImportType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportType value: {data!r}")
    return cast(ImportType, data)
