"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#Regions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.region

Regions: TypeAlias = list["capo_route53globalresolver.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: Regions) -> list:
    return list(value)


def deserialize_json(data: list) -> Regions:
    return list(data)
