"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpRouteStatusMsg``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

IpRouteStatusMsg: TypeAlias = Literal[
    "Adding",
    "Added",
    "Removing",
    "Removed",
    "AddFailed",
    "RemoveFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Adding",
        "Added",
        "Removing",
        "Removed",
        "AddFailed",
        "RemoveFailed",
    )
)


def serialize_aws_json_1_1(value: IpRouteStatusMsg) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpRouteStatusMsg:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpRouteStatusMsg value: {data!r}")
    return cast(IpRouteStatusMsg, data)
