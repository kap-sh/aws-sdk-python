"""Generated from Smithy shape ``com.amazonaws.datasync#LocationFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

LocationFilterName: TypeAlias = Literal[
    "LocationUri",
    "LocationType",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LocationUri",
        "LocationType",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: LocationFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocationFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LocationFilterName value: {data!r}")
    return cast(LocationFilterName, data)
