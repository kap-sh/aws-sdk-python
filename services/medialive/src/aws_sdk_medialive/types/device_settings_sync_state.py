"""Generated from Smithy shape ``com.amazonaws.medialive#DeviceSettingsSyncState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The status of the action to synchronize the device configuration. If you change the configuration of the input device (for example, the maximum bitrate), MediaLive sends the new data to the device. The device might not update itself immediately. SYNCED means the device has updated its configuration. SYNCING means that it has not updated its configuration."""
DeviceSettingsSyncState: TypeAlias = Literal[
    "SYNCED",
    "SYNCING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYNCED",
        "SYNCING",
    )
)


def serialize_json(value: DeviceSettingsSyncState) -> str:
    return value


def deserialize_json(data: str) -> DeviceSettingsSyncState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceSettingsSyncState value: {data!r}")
    return cast(DeviceSettingsSyncState, data)
