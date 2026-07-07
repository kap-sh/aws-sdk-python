"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteEventTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class DeleteEventTriggerRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_trigger_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the event trigger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventTriggerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventTriggerRequest:
    out: DeleteEventTriggerRequest = {}  # type: ignore[typeddict-item]
    return out
