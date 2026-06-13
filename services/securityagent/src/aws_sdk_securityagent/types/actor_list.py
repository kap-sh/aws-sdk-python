"""Generated from Smithy shape ``com.amazonaws.securityagent#ActorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.actor

ActorList: TypeAlias = list["aws_sdk_securityagent.types.actor.Actor"]


# --- restJson1 ser/de ---
def serialize_json(value: ActorList) -> list:
    import aws_sdk_securityagent.types.actor

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.actor.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActorList:
    import aws_sdk_securityagent.types.actor

    out: ActorList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.actor.deserialize_json(item))
    return out
