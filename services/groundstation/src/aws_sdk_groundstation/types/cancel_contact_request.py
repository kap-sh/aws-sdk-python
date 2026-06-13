"""Generated from Smithy shape ``com.amazonaws.groundstation#CancelContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class CancelContactRequest(TypedDict):
    contact_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelContactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelContactRequest:
    out: CancelContactRequest = {}  # type: ignore[typeddict-item]
    return out
