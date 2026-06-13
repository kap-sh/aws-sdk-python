"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetMedicalScribeListeningSessionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.scribe_session_id
    import aws_sdk_connecthealth.types.subscription_id


class GetMedicalScribeListeningSessionInput(TypedDict):
    session_id: "aws_sdk_connecthealth.types.scribe_session_id.ScribeSessionId"
    """<p>The Session identifier</p>"""
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p>The Domain identifier</p>"""
    subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId"
    """<p>The Subscription identifier</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalScribeListeningSessionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMedicalScribeListeningSessionInput:
    out: GetMedicalScribeListeningSessionInput = {}  # type: ignore[typeddict-item]
    return out
