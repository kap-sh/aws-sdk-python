"""Generated from Smithy shape ``com.amazonaws.appstream#FleetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

FleetType: TypeAlias = Literal[
    "ALWAYS_ON",
    "ON_DEMAND",
    "ELASTIC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS_ON",
        "ON_DEMAND",
        "ELASTIC",
    )
)


def serialize_aws_json_1_1(value: FleetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetType value: {data!r}")
    return cast(FleetType, data)
