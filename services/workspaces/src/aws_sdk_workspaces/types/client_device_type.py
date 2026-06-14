"""Generated from Smithy shape ``com.amazonaws.workspaces#ClientDeviceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

ClientDeviceType: TypeAlias = Literal[
    "DeviceTypeWindows",
    "DeviceTypeOsx",
    "DeviceTypeAndroid",
    "DeviceTypeIos",
    "DeviceTypeLinux",
    "DeviceTypeWeb",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DeviceTypeWindows",
        "DeviceTypeOsx",
        "DeviceTypeAndroid",
        "DeviceTypeIos",
        "DeviceTypeLinux",
        "DeviceTypeWeb",
    )
)


def serialize_aws_json_1_1(value: ClientDeviceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientDeviceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientDeviceType value: {data!r}")
    return cast(ClientDeviceType, data)
