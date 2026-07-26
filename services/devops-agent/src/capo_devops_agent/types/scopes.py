"""Generated from Smithy shape ``com.amazonaws.devopsagent#Scopes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.o_auth_scope

Scopes: TypeAlias = list["capo_devops_agent.types.o_auth_scope.OAuthScope"]


# --- restJson1 ser/de ---
def serialize_json(value: Scopes) -> list:
    return list(value)


def deserialize_json(data: list) -> Scopes:
    return list(data)
