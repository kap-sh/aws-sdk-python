"""Generated from Smithy shape ``com.amazonaws.ssm#PatchProperty``."""

from typing import Literal, TypeAlias, cast

PatchProperty: TypeAlias = Literal[
    "PRODUCT",
    "PRODUCT_FAMILY",
    "CLASSIFICATION",
    "MSRC_SEVERITY",
    "PRIORITY",
    "SEVERITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchProperty) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchProperty:
    return cast(PatchProperty, data)
