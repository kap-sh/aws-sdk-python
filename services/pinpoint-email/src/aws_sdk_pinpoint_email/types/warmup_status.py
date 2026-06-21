"""Generated from Smithy shape ``com.amazonaws.pinpointemail#WarmupStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The warmup status of a dedicated IP.</p>"""
WarmupStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "DONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: WarmupStatus) -> str:
    return value


def deserialize_json(data: str) -> WarmupStatus:
    return cast(WarmupStatus, data)
