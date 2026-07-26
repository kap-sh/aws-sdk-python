"""Generated from Smithy shape ``com.amazonaws.guardduty#Actor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.actor_process
    import capo_guardduty.types.session
    import capo_guardduty.types.string
    import capo_guardduty.types.user


class Actor(TypedDict, closed=True):
    id: NotRequired["capo_guardduty.types.string.String"]
    """<p>ID of the threat actor.</p>"""
    user: NotRequired["capo_guardduty.types.user.User"]
    """<p>Contains information about the user credentials used by the threat actor.</p>"""
    session: NotRequired["capo_guardduty.types.session.Session"]
    """<p>Contains information about the user session where the activity initiated.</p>"""
    process: NotRequired["capo_guardduty.types.actor_process.ActorProcess"]
    """<p>Contains information about the process associated with the threat actor. This includes details such as process name, path, execution time, and unique identifiers that help track the actor's activities within the system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Actor) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "user" in value:
        import capo_guardduty.types.user

        out["user"] = capo_guardduty.types.user.serialize_json(value["user"])
    if "session" in value:
        import capo_guardduty.types.session

        out["session"] = capo_guardduty.types.session.serialize_json(value["session"])
    if "process" in value:
        import capo_guardduty.types.actor_process

        out["process"] = capo_guardduty.types.actor_process.serialize_json(
            value["process"]
        )
    return out


def deserialize_json(data: dict) -> Actor:
    out: Actor = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "user" in data:
        import capo_guardduty.types.user

        out["user"] = capo_guardduty.types.user.deserialize_json(data["user"])
    if "session" in data:
        import capo_guardduty.types.session

        out["session"] = capo_guardduty.types.session.deserialize_json(data["session"])
    if "process" in data:
        import capo_guardduty.types.actor_process

        out["process"] = capo_guardduty.types.actor_process.deserialize_json(
            data["process"]
        )
    return out
