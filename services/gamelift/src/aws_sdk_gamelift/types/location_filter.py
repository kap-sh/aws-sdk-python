"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

LocationFilter: TypeAlias = Literal[
    "AWS",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "CUSTOM",
    )
)


def serialize_aws_json_1_1(value: LocationFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocationFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LocationFilter value: {data!r}")
    return cast(LocationFilter, data)
