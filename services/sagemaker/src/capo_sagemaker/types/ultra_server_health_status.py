"""Generated from Smithy shape ``com.amazonaws.sagemaker#UltraServerHealthStatus``."""

from typing import Literal, TypeAlias, cast

UltraServerHealthStatus: TypeAlias = Literal[
    "OK",
    "Impaired",
    "Insufficient-Data",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UltraServerHealthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UltraServerHealthStatus:
    return cast(UltraServerHealthStatus, data)
