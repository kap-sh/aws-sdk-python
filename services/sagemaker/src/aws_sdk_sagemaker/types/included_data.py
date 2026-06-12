"""Generated from Smithy shape ``com.amazonaws.sagemaker#IncludedData``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

IncludedData: TypeAlias = Literal[
    "AllData",
    "MetadataOnly",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AllData",
        "MetadataOnly",
    )
)


def serialize_aws_json_1_1(value: IncludedData) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IncludedData:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludedData value: {data!r}")
    return cast(IncludedData, data)
