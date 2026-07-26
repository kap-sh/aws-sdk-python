"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserActionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a browser action execution.</p>"""
BrowserActionStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserActionStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserActionStatus:
    return cast(BrowserActionStatus, data)
