"""Generated from Smithy shape ``com.amazonaws.iotwireless#MulticastFrameInfo``."""

from typing import Literal, TypeAlias, cast

"""<p> <code>FrameInfo</code> of your multicast group resources for the trace content. Use FrameInfo to debug the multicast communication between your multicast groups and the network server.</p>"""
MulticastFrameInfo: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastFrameInfo) -> str:
    return value


def deserialize_json(data: str) -> MulticastFrameInfo:
    return cast(MulticastFrameInfo, data)
