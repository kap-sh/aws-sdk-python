"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetSortByType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetSortByType: TypeAlias = Literal[
    "NAME",
    "CREATED_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "CREATED_TIME",
        "LAST_MODIFIED_TIME",
    )
)


def serialize_aws_json_1_1(value: FleetSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetSortByType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetSortByType value: {data!r}")
    return cast(FleetSortByType, data)
