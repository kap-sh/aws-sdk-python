"""Generated from Smithy shape ``com.amazonaws.mgn#ParticipatingServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.participating_server

ParticipatingServers: TypeAlias = list[
    "capo_mgn.types.participating_server.ParticipatingServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingServers) -> list:
    import capo_mgn.types.participating_server

    out: list = []
    for item in value:
        out.append(capo_mgn.types.participating_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipatingServers:
    import capo_mgn.types.participating_server

    out: ParticipatingServers = []
    for item in data:
        out.append(capo_mgn.types.participating_server.deserialize_json(item))
    return out
