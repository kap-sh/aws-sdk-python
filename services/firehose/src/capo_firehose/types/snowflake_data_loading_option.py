"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeDataLoadingOption``."""

from typing import Literal, TypeAlias, cast

SnowflakeDataLoadingOption: TypeAlias = Literal[
    "JSON_MAPPING",
    "VARIANT_CONTENT_MAPPING",
    "VARIANT_CONTENT_AND_METADATA_MAPPING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeDataLoadingOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnowflakeDataLoadingOption:
    return cast(SnowflakeDataLoadingOption, data)
