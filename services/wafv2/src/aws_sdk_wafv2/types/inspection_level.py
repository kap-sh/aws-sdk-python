"""Generated from Smithy shape ``com.amazonaws.wafv2#InspectionLevel``."""

from typing import Literal, TypeAlias, cast

InspectionLevel: TypeAlias = Literal[
    "COMMON",
    "TARGETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InspectionLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InspectionLevel:
    return cast(InspectionLevel, data)
