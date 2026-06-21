"""Generated from Smithy shape ``com.amazonaws.macie2#MacieStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an Amazon Macie account. Valid values are:</p>"""
MacieStatus: TypeAlias = Literal[
    "PAUSED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MacieStatus) -> str:
    return value


def deserialize_json(data: str) -> MacieStatus:
    return cast(MacieStatus, data)
