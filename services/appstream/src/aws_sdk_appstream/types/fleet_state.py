"""Generated from Smithy shape ``com.amazonaws.appstream#FleetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

FleetState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: FleetState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetState value: {data!r}")
    return cast(FleetState, data)
