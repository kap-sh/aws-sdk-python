"""Generated from Smithy shape ``com.amazonaws.securityhub#Actor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.actor_session
    import capo_securityhub.types.actor_user
    import capo_securityhub.types.non_empty_string


class Actor(TypedDict, closed=True):
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the threat actor. </p>"""
    user: NotRequired["capo_securityhub.types.actor_user.ActorUser"]
    """<p> Contains information about the user credentials used by the threat actor.</p>"""
    session: NotRequired["capo_securityhub.types.actor_session.ActorSession"]
    """<p> Contains information about the user session where the activity initiated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Actor) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "user" in value:
        import capo_securityhub.types.actor_user

        out["User"] = capo_securityhub.types.actor_user.serialize_json(value["user"])
    if "session" in value:
        import capo_securityhub.types.actor_session

        out["Session"] = capo_securityhub.types.actor_session.serialize_json(
            value["session"]
        )
    return out


def deserialize_json(data: dict) -> Actor:
    out: Actor = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "User" in data:
        import capo_securityhub.types.actor_user

        out["user"] = capo_securityhub.types.actor_user.deserialize_json(data["User"])
    if "Session" in data:
        import capo_securityhub.types.actor_session

        out["session"] = capo_securityhub.types.actor_session.deserialize_json(
            data["Session"]
        )
    return out
