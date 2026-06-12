"""Generated from Smithy shape ``com.amazonaws.sfn#IncludedData``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

IncludedData: TypeAlias = Literal[
    "ALL_DATA",
    "METADATA_ONLY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_DATA",
        "METADATA_ONLY",
    )
)


def serialize_aws_json_1_0(value: IncludedData) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IncludedData:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludedData value: {data!r}")
    return cast(IncludedData, data)
