"""Generated from Smithy shape ``com.amazonaws.iotwireless#MulticastFrameInfo``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p> <code>FrameInfo</code> of your multicast group resources for the trace content. Use FrameInfo to debug the multicast communication between your multicast groups and the network server.</p>"""
MulticastFrameInfo: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: MulticastFrameInfo) -> str:
    return value


def deserialize_json(data: str) -> MulticastFrameInfo:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MulticastFrameInfo value: {data!r}")
    return cast(MulticastFrameInfo, data)
