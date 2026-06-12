"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GlobalResolvers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.global_resolvers_item

GlobalResolvers: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.global_resolvers_item.GlobalResolversItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalResolvers) -> list:
    import aws_sdk_route53globalresolver.types.global_resolvers_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.global_resolvers_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GlobalResolvers:
    import aws_sdk_route53globalresolver.types.global_resolvers_item

    out: GlobalResolvers = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.global_resolvers_item.deserialize_json(
                item
            )
        )
    return out
