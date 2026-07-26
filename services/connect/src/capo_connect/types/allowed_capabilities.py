"""Generated from Smithy shape ``com.amazonaws.connect#AllowedCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.participant_capabilities


class AllowedCapabilities(TypedDict, closed=True):
    customer: NotRequired[
        "capo_connect.types.participant_capabilities.ParticipantCapabilities"
    ]
    """<p>Information about the customer's video sharing capabilities.</p>"""
    agent: NotRequired[
        "capo_connect.types.participant_capabilities.ParticipantCapabilities"
    ]
    """<p>Information about the agent's video sharing capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedCapabilities) -> dict:
    out: dict = {}
    if "customer" in value:
        import capo_connect.types.participant_capabilities

        out["Customer"] = capo_connect.types.participant_capabilities.serialize_json(
            value["customer"]
        )
    if "agent" in value:
        import capo_connect.types.participant_capabilities

        out["Agent"] = capo_connect.types.participant_capabilities.serialize_json(
            value["agent"]
        )
    return out


def deserialize_json(data: dict) -> AllowedCapabilities:
    out: AllowedCapabilities = {}  # type: ignore[typeddict-item]
    if "Customer" in data:
        import capo_connect.types.participant_capabilities

        out["customer"] = capo_connect.types.participant_capabilities.deserialize_json(
            data["Customer"]
        )
    if "Agent" in data:
        import capo_connect.types.participant_capabilities

        out["agent"] = capo_connect.types.participant_capabilities.deserialize_json(
            data["Agent"]
        )
    return out
