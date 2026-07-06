"""Generated from Smithy shape ``com.amazonaws.omics#AcceptShareRequest``."""

from typing_extensions import TypedDict


class AcceptShareRequest(TypedDict, closed=True):
    share_id: "str"
    """<p>The ID of the resource share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptShareRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AcceptShareRequest:
    out: AcceptShareRequest = {}  # type: ignore[typeddict-item]
    return out
