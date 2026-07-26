"""Generated from Smithy shape ``com.amazonaws.kms#KeyMaterialState``."""

from typing import Literal, TypeAlias, cast

KeyMaterialState: TypeAlias = Literal[
    "NON_CURRENT",
    "CURRENT",
    "PENDING_ROTATION",
    "PENDING_MULTI_REGION_IMPORT_AND_ROTATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyMaterialState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyMaterialState:
    return cast(KeyMaterialState, data)
