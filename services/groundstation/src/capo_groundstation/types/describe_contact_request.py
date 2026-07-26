"""Generated from Smithy shape ``com.amazonaws.groundstation#DescribeContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid


class DescribeContactRequest(TypedDict, closed=True):
    contact_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeContactRequest:
    out: DescribeContactRequest = {}  # type: ignore[typeddict-item]
    return out
