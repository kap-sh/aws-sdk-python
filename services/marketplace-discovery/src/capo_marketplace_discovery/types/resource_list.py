"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.resource

ResourceList: TypeAlias = list["capo_marketplace_discovery.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceList) -> list:
    import capo_marketplace_discovery.types.resource

    out: list = []
    for item in value:
        out.append(capo_marketplace_discovery.types.resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceList:
    import capo_marketplace_discovery.types.resource

    out: ResourceList = []
    for item in data:
        out.append(capo_marketplace_discovery.types.resource.deserialize_json(item))
    return out
