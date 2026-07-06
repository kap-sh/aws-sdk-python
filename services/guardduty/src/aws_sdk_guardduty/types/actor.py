"""Generated from Smithy shape ``com.amazonaws.guardduty#Actor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.actor_process
    import aws_sdk_guardduty.types.session
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.user


class Actor(TypedDict, closed=True):
    id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>ID of the threat actor.</p>"""
    user: NotRequired["aws_sdk_guardduty.types.user.User"]
    """<p>Contains information about the user credentials used by the threat actor.</p>"""
    session: NotRequired["aws_sdk_guardduty.types.session.Session"]
    """<p>Contains information about the user session where the activity initiated.</p>"""
    process: NotRequired["aws_sdk_guardduty.types.actor_process.ActorProcess"]
    """<p>Contains information about the process associated with the threat actor. This includes details such as process name, path, execution time, and unique identifiers that help track the actor's activities within the system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Actor) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "user" in value:
        import aws_sdk_guardduty.types.user

        out["user"] = aws_sdk_guardduty.types.user.serialize_json(value["user"])
    if "session" in value:
        import aws_sdk_guardduty.types.session

        out["session"] = aws_sdk_guardduty.types.session.serialize_json(
            value["session"]
        )
    if "process" in value:
        import aws_sdk_guardduty.types.actor_process

        out["process"] = aws_sdk_guardduty.types.actor_process.serialize_json(
            value["process"]
        )
    return out


def deserialize_json(data: dict) -> Actor:
    out: Actor = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "user" in data:
        import aws_sdk_guardduty.types.user

        out["user"] = aws_sdk_guardduty.types.user.deserialize_json(data["user"])
    if "session" in data:
        import aws_sdk_guardduty.types.session

        out["session"] = aws_sdk_guardduty.types.session.deserialize_json(
            data["session"]
        )
    if "process" in data:
        import aws_sdk_guardduty.types.actor_process

        out["process"] = aws_sdk_guardduty.types.actor_process.deserialize_json(
            data["process"]
        )
    return out
