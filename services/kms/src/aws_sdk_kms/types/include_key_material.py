"""Generated from Smithy shape ``com.amazonaws.kms#IncludeKeyMaterial``."""

from typing import Literal, TypeAlias, cast

IncludeKeyMaterial: TypeAlias = Literal[
    "ALL_KEY_MATERIAL",
    "ROTATIONS_ONLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncludeKeyMaterial) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IncludeKeyMaterial:
    return cast(IncludeKeyMaterial, data)
