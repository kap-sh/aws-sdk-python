"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#Domains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.domain

Domains: TypeAlias = list["capo_route53globalresolver.types.domain.Domain"]


# --- restJson1 ser/de ---
def serialize_json(value: Domains) -> list:
    return list(value)


def deserialize_json(data: list) -> Domains:
    return list(data)
