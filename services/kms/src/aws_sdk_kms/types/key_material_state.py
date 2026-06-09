"""Generated from Smithy shape ``com.amazonaws.kms#KeyMaterialState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

KeyMaterialState: TypeAlias = Literal[
    "NON_CURRENT",
    "CURRENT",
    "PENDING_ROTATION",
    "PENDING_MULTI_REGION_IMPORT_AND_ROTATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NON_CURRENT",
        "CURRENT",
        "PENDING_ROTATION",
        "PENDING_MULTI_REGION_IMPORT_AND_ROTATION",
    )
)


def serialize_aws_json_1_1(value: KeyMaterialState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyMaterialState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyMaterialState value: {data!r}")
    return cast(KeyMaterialState, data)
