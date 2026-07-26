"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetMedicalScribeListeningSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.scribe_session_id
    import capo_connecthealth.types.subscription_id


class GetMedicalScribeListeningSessionInput(TypedDict, closed=True):
    session_id: "capo_connecthealth.types.scribe_session_id.ScribeSessionId"
    """<p>The Session identifier</p>"""
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The Domain identifier</p>"""
    subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId"
    """<p>The Subscription identifier</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalScribeListeningSessionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMedicalScribeListeningSessionInput:
    out: GetMedicalScribeListeningSessionInput = {}  # type: ignore[typeddict-item]
    return out
