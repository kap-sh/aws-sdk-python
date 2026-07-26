"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#AccessSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.access_sources_item

AccessSources: TypeAlias = list[
    "capo_route53globalresolver.types.access_sources_item.AccessSourcesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessSources) -> list:
    import capo_route53globalresolver.types.access_sources_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.access_sources_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccessSources:
    import capo_route53globalresolver.types.access_sources_item

    out: AccessSources = []
    for item in data:
        out.append(
            capo_route53globalresolver.types.access_sources_item.deserialize_json(item)
        )
    return out
