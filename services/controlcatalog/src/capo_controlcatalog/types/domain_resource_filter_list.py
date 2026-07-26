"""Generated from Smithy shape ``com.amazonaws.controlcatalog#DomainResourceFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.domain_resource_filter

DomainResourceFilterList: TypeAlias = list[
    "capo_controlcatalog.types.domain_resource_filter.DomainResourceFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainResourceFilterList) -> list:
    import capo_controlcatalog.types.domain_resource_filter

    out: list = []
    for item in value:
        out.append(
            capo_controlcatalog.types.domain_resource_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DomainResourceFilterList:
    import capo_controlcatalog.types.domain_resource_filter

    out: DomainResourceFilterList = []
    for item in data:
        out.append(
            capo_controlcatalog.types.domain_resource_filter.deserialize_json(item)
        )
    return out
