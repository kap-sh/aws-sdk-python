"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EventActor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.actor_type


class EventActor(TypedDict):
    type: "aws_sdk_resiliencehubv2.types.actor_type.ActorType"
    """<p>The type of actor, either USER or SYSTEM.</p>"""
    principal_id: "str"
    """<p>The principal ID of the actor.</p>"""
    account_id: NotRequired["str"]
    """<p>The AWS account ID of the actor.</p>"""
    user_name: NotRequired["str"]
    """<p>The user name of the actor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventActor) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.actor_type

    out["type"] = aws_sdk_resiliencehubv2.types.actor_type.serialize_json(value["type"])
    out["principalId"] = value["principal_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    return out


def deserialize_json(data: dict) -> EventActor:
    out: EventActor = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_resiliencehubv2.types.actor_type

        out["type"] = aws_sdk_resiliencehubv2.types.actor_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("EventActor.type required")
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    else:
        raise DeserializationError("EventActor.principal_id required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "userName" in data:
        out["user_name"] = data["userName"]
    return out
