"""Generated from Smithy shape ``com.amazonaws.glue#CatalogEncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CatalogEncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "SSE-KMS",
    "SSE-KMS-WITH-SERVICE-ROLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "SSE-KMS",
        "SSE-KMS-WITH-SERVICE-ROLE",
    )
)


def serialize_aws_json_1_1(value: CatalogEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CatalogEncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CatalogEncryptionMode value: {data!r}")
    return cast(CatalogEncryptionMode, data)
