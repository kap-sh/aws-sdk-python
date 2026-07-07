"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetEventTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class GetEventTriggerRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_trigger_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the event trigger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventTriggerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventTriggerRequest:
    out: GetEventTriggerRequest = {}  # type: ignore[typeddict-item]
    return out
