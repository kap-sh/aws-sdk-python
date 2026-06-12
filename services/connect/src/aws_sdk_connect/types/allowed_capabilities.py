"""Generated from Smithy shape ``com.amazonaws.connect#AllowedCapabilities``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.participant_capabilities


class AllowedCapabilities(TypedDict):
    customer: NotRequired[
        "aws_sdk_connect.types.participant_capabilities.ParticipantCapabilities"
    ]
    """<p>Information about the customer's video sharing capabilities.</p>"""
    agent: NotRequired[
        "aws_sdk_connect.types.participant_capabilities.ParticipantCapabilities"
    ]
    """<p>Information about the agent's video sharing capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedCapabilities) -> dict:
    out: dict = {}
    if "customer" in value:
        import aws_sdk_connect.types.participant_capabilities

        out["Customer"] = aws_sdk_connect.types.participant_capabilities.serialize_json(
            value["customer"]
        )
    if "agent" in value:
        import aws_sdk_connect.types.participant_capabilities

        out["Agent"] = aws_sdk_connect.types.participant_capabilities.serialize_json(
            value["agent"]
        )
    return out


def deserialize_json(data: dict) -> AllowedCapabilities:
    out: AllowedCapabilities = {}  # type: ignore[typeddict-item]
    if "Customer" in data:
        import aws_sdk_connect.types.participant_capabilities

        out["customer"] = (
            aws_sdk_connect.types.participant_capabilities.deserialize_json(
                data["Customer"]
            )
        )
    if "Agent" in data:
        import aws_sdk_connect.types.participant_capabilities

        out["agent"] = aws_sdk_connect.types.participant_capabilities.deserialize_json(
            data["Agent"]
        )
    return out
