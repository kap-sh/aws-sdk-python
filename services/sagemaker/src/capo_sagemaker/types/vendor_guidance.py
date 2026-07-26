"""Generated from Smithy shape ``com.amazonaws.sagemaker#VendorGuidance``."""

from typing import Literal, TypeAlias, cast

VendorGuidance: TypeAlias = Literal[
    "NOT_PROVIDED",
    "STABLE",
    "TO_BE_ARCHIVED",
    "ARCHIVED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VendorGuidance) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VendorGuidance:
    return cast(VendorGuidance, data)
