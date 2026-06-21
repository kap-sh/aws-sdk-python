"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserProfileStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a browser profile.</p>"""
BrowserProfileStatus: TypeAlias = Literal[
    "READY",
    "DELETING",
    "DELETED",
    "SAVING",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserProfileStatus:
    return cast(BrowserProfileStatus, data)
