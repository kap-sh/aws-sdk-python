"""Generated from Smithy shape ``com.amazonaws.macie2#PolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.finding_action
    import capo_macie2.types.finding_actor


class PolicyDetails(TypedDict, closed=True):
    action: NotRequired["capo_macie2.types.finding_action.FindingAction"]
    """<p>The action that produced the finding.</p>"""
    actor: NotRequired["capo_macie2.types.finding_actor.FindingActor"]
    """<p>The entity that performed the action that produced the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDetails) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_macie2.types.finding_action

        out["action"] = capo_macie2.types.finding_action.serialize_json(value["action"])
    if "actor" in value:
        import capo_macie2.types.finding_actor

        out["actor"] = capo_macie2.types.finding_actor.serialize_json(value["actor"])
    return out


def deserialize_json(data: dict) -> PolicyDetails:
    out: PolicyDetails = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import capo_macie2.types.finding_action

        out["action"] = capo_macie2.types.finding_action.deserialize_json(
            data["action"]
        )
    if "actor" in data:
        import capo_macie2.types.finding_actor

        out["actor"] = capo_macie2.types.finding_actor.deserialize_json(data["actor"])
    return out
