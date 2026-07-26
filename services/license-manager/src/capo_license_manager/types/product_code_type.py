"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductCodeType``."""

from typing import Literal, TypeAlias, cast

ProductCodeType: TypeAlias = Literal["marketplace",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductCodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductCodeType:
    return cast(ProductCodeType, data)
