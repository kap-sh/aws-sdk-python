"""Generated from Smithy shape ``com.amazonaws.datasync#AzureAccessTier``."""

from typing import Literal, TypeAlias, cast

AzureAccessTier: TypeAlias = Literal[
    "HOT",
    "COOL",
    "ARCHIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureAccessTier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AzureAccessTier:
    return cast(AzureAccessTier, data)
