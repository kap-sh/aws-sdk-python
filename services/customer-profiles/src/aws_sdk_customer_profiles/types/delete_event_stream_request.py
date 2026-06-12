"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteEventStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class DeleteEventStreamRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_stream_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the event stream</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventStreamRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventStreamRequest:
    out: DeleteEventStreamRequest = {}  # type: ignore[typeddict-item]
    return out
