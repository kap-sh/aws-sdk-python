"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationContactParticipant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_participant_role
    import capo_connect.types.resource_id


class EvaluationContactParticipant(TypedDict, closed=True):
    contact_participant_role: NotRequired[
        "capo_connect.types.contact_participant_role.ContactParticipantRole"
    ]
    """<p>The role of the contact participant.</p>"""
    contact_participant_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The identifier for the contact participant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationContactParticipant) -> dict:
    out: dict = {}
    if "contact_participant_role" in value:
        import capo_connect.types.contact_participant_role

        out["ContactParticipantRole"] = (
            capo_connect.types.contact_participant_role.serialize_json(
                value["contact_participant_role"]
            )
        )
    if "contact_participant_id" in value:
        out["ContactParticipantId"] = value["contact_participant_id"]
    return out


def deserialize_json(data: dict) -> EvaluationContactParticipant:
    out: EvaluationContactParticipant = {}  # type: ignore[typeddict-item]
    if "ContactParticipantRole" in data:
        import capo_connect.types.contact_participant_role

        out["contact_participant_role"] = (
            capo_connect.types.contact_participant_role.deserialize_json(
                data["ContactParticipantRole"]
            )
        )
    if "ContactParticipantId" in data:
        out["contact_participant_id"] = data["ContactParticipantId"]
    return out
