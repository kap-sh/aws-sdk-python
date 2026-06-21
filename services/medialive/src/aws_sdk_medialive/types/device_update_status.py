"""Generated from Smithy shape ``com.amazonaws.medialive#DeviceUpdateStatus``."""

from typing import Literal, TypeAlias, cast

"""The status of software on the input device."""
DeviceUpdateStatus: TypeAlias = Literal[
    "UP_TO_DATE",
    "NOT_UP_TO_DATE",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> DeviceUpdateStatus:
    return cast(DeviceUpdateStatus, data)
