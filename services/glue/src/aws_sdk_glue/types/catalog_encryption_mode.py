"""Generated from Smithy shape ``com.amazonaws.glue#CatalogEncryptionMode``."""

from typing import Literal, TypeAlias, cast

CatalogEncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "SSE-KMS",
    "SSE-KMS-WITH-SERVICE-ROLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CatalogEncryptionMode:
    return cast(CatalogEncryptionMode, data)
