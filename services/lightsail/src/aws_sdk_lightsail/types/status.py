"""Generated from Smithy shape ``com.amazonaws.lightsail#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

Status: TypeAlias = Literal[
    "startExpired",
    "notStarted",
    "started",
    "starting",
    "stopped",
    "stopping",
    "settingUpInstance",
    "failedInstanceCreation",
    "failedStartingGUISession",
    "failedStoppingGUISession",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "startExpired",
        "notStarted",
        "started",
        "starting",
        "stopped",
        "stopping",
        "settingUpInstance",
        "failedInstanceCreation",
        "failedStartingGUISession",
        "failedStoppingGUISession",
    )
)


def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
