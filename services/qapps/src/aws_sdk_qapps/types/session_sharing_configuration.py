"""Generated from Smithy shape ``com.amazonaws.qapps#SessionSharingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.session_sharing_accept_responses
    import aws_sdk_qapps.types.session_sharing_enabled
    import aws_sdk_qapps.types.session_sharing_reveal_cards


class SessionSharingConfiguration(TypedDict, closed=True):
    enabled: "aws_sdk_qapps.types.session_sharing_enabled.SessionSharingEnabled"
    """<p>Indicates whether an Q App session is shareable with other users.</p>"""
    accept_responses: NotRequired[
        "aws_sdk_qapps.types.session_sharing_accept_responses.SessionSharingAcceptResponses"
    ]
    """<p>Indicates whether an Q App session can accept responses from users.</p>"""
    reveal_cards: NotRequired[
        "aws_sdk_qapps.types.session_sharing_reveal_cards.SessionSharingRevealCards"
    ]
    """<p>Indicates whether collected responses for an Q App session are revealed for all users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSharingConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "accept_responses" in value:
        out["acceptResponses"] = value["accept_responses"]
    if "reveal_cards" in value:
        out["revealCards"] = value["reveal_cards"]
    return out


def deserialize_json(data: dict) -> SessionSharingConfiguration:
    out: SessionSharingConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("SessionSharingConfiguration.enabled required")
    if "acceptResponses" in data:
        out["accept_responses"] = data["acceptResponses"]
    if "revealCards" in data:
        out["reveal_cards"] = data["revealCards"]
    return out
