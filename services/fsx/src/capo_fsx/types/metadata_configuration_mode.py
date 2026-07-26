"""Generated from Smithy shape ``com.amazonaws.fsx#MetadataConfigurationMode``."""

from typing import Literal, TypeAlias, cast

MetadataConfigurationMode: TypeAlias = Literal[
    "AUTOMATIC",
    "USER_PROVISIONED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataConfigurationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetadataConfigurationMode:
    return cast(MetadataConfigurationMode, data)
