"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeDataLoadingOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

SnowflakeDataLoadingOption: TypeAlias = Literal[
    "JSON_MAPPING",
    "VARIANT_CONTENT_MAPPING",
    "VARIANT_CONTENT_AND_METADATA_MAPPING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON_MAPPING",
        "VARIANT_CONTENT_MAPPING",
        "VARIANT_CONTENT_AND_METADATA_MAPPING",
    )
)


def serialize_aws_json_1_1(value: SnowflakeDataLoadingOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnowflakeDataLoadingOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SnowflakeDataLoadingOption value: {data!r}"
        )
    return cast(SnowflakeDataLoadingOption, data)
