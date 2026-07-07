"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetEventStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class GetEventStreamRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_stream_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the event stream provided during create operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventStreamRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventStreamRequest:
    out: GetEventStreamRequest = {}  # type: ignore[typeddict-item]
    return out
