"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GlobalResolvers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.global_resolvers_item

GlobalResolvers: TypeAlias = list[
    "capo_route53globalresolver.types.global_resolvers_item.GlobalResolversItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalResolvers) -> list:
    import capo_route53globalresolver.types.global_resolvers_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.global_resolvers_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GlobalResolvers:
    import capo_route53globalresolver.types.global_resolvers_item

    out: GlobalResolvers = []
    for item in data:
        out.append(
            capo_route53globalresolver.types.global_resolvers_item.deserialize_json(
                item
            )
        )
    return out
