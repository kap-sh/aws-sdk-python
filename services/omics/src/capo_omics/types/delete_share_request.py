"""Generated from Smithy shape ``com.amazonaws.omics#DeleteShareRequest``."""

from typing_extensions import TypedDict


class DeleteShareRequest(TypedDict, closed=True):
    share_id: "str"
    """<p>The ID for the resource share to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteShareRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteShareRequest:
    out: DeleteShareRequest = {}  # type: ignore[typeddict-item]
    return out
