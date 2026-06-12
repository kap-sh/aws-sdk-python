"""Generated from Smithy shape ``com.amazonaws.securityhub#ActorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.actor

ActorsList: TypeAlias = list["aws_sdk_securityhub.types.actor.Actor"]


# --- restJson1 ser/de ---
def serialize_json(value: ActorsList) -> list:
    import aws_sdk_securityhub.types.actor

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.actor.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActorsList:
    import aws_sdk_securityhub.types.actor

    out: ActorsList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.actor.deserialize_json(item))
    return out
