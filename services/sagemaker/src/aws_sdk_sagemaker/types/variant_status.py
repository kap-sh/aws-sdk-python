"""Generated from Smithy shape ``com.amazonaws.sagemaker#VariantStatus``."""

from typing import Literal, TypeAlias, cast

VariantStatus: TypeAlias = Literal[
    "Creating",
    "Updating",
    "Deleting",
    "ActivatingTraffic",
    "Baking",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariantStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VariantStatus:
    return cast(VariantStatus, data)
