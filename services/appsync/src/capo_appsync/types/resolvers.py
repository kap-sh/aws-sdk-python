"""Generated from Smithy shape ``com.amazonaws.appsync#Resolvers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.resolver

Resolvers: TypeAlias = list["capo_appsync.types.resolver.Resolver"]


# --- restJson1 ser/de ---
def serialize_json(value: Resolvers) -> list:
    import capo_appsync.types.resolver

    out: list = []
    for item in value:
        out.append(capo_appsync.types.resolver.serialize_json(item))
    return out


def deserialize_json(data: list) -> Resolvers:
    import capo_appsync.types.resolver

    out: Resolvers = []
    for item in data:
        out.append(capo_appsync.types.resolver.deserialize_json(item))
    return out
