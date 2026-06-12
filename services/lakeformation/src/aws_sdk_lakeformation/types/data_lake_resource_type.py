"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataLakeResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

DataLakeResourceType: TypeAlias = Literal[
    "CATALOG",
    "DATABASE",
    "TABLE",
    "DATA_LOCATION",
    "LF_TAG",
    "LF_TAG_POLICY",
    "LF_TAG_POLICY_DATABASE",
    "LF_TAG_POLICY_TABLE",
    "LF_NAMED_TAG_EXPRESSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CATALOG",
        "DATABASE",
        "TABLE",
        "DATA_LOCATION",
        "LF_TAG",
        "LF_TAG_POLICY",
        "LF_TAG_POLICY_DATABASE",
        "LF_TAG_POLICY_TABLE",
        "LF_NAMED_TAG_EXPRESSION",
    )
)


def serialize_json(value: DataLakeResourceType) -> str:
    return value


def deserialize_json(data: str) -> DataLakeResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataLakeResourceType value: {data!r}")
    return cast(DataLakeResourceType, data)
