"""Generated from Smithy shape ``com.amazonaws.qconnect#SystemEndpointAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attribute_value


class SystemEndpointAttributes(TypedDict, closed=True):
    address: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's phone number if used with <code>customerEndpoint</code>, or the number the customer dialed to call your contact center if used with <code>systemEndpoint</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemEndpointAttributes) -> dict:
    out: dict = {}
    if "address" in value:
        out["address"] = value["address"]
    return out


def deserialize_json(data: dict) -> SystemEndpointAttributes:
    out: SystemEndpointAttributes = {}  # type: ignore[typeddict-item]
    if "address" in data:
        out["address"] = data["address"]
    return out
