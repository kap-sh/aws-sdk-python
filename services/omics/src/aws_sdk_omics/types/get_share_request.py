"""Generated from Smithy shape ``com.amazonaws.omics#GetShareRequest``."""

from typing_extensions import TypedDict


class GetShareRequest(TypedDict, closed=True):
    share_id: "str"
    """<p>The ID of the share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetShareRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetShareRequest:
    out: GetShareRequest = {}  # type: ignore[typeddict-item]
    return out
