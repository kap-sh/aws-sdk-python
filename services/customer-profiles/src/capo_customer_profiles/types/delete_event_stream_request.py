"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteEventStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class DeleteEventStreamRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_stream_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the event stream</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventStreamRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventStreamRequest:
    out: DeleteEventStreamRequest = {}  # type: ignore[typeddict-item]
    return out
