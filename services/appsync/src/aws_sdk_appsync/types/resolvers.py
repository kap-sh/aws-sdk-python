"""Generated from Smithy shape ``com.amazonaws.appsync#Resolvers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resolver

Resolvers: TypeAlias = list["aws_sdk_appsync.types.resolver.Resolver"]


# --- restJson1 ser/de ---
def serialize_json(value: Resolvers) -> list:
    import aws_sdk_appsync.types.resolver

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.resolver.serialize_json(item))
    return out


def deserialize_json(data: list) -> Resolvers:
    import aws_sdk_appsync.types.resolver

    out: Resolvers = []
    for item in data:
        out.append(aws_sdk_appsync.types.resolver.deserialize_json(item))
    return out
