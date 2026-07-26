"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainMaintenanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.domain_maintenance_details

DomainMaintenanceList: TypeAlias = list[
    "capo_opensearch.types.domain_maintenance_details.DomainMaintenanceDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainMaintenanceList) -> list:
    import capo_opensearch.types.domain_maintenance_details

    out: list = []
    for item in value:
        out.append(
            capo_opensearch.types.domain_maintenance_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DomainMaintenanceList:
    import capo_opensearch.types.domain_maintenance_details

    out: DomainMaintenanceList = []
    for item in data:
        out.append(
            capo_opensearch.types.domain_maintenance_details.deserialize_json(item)
        )
    return out
