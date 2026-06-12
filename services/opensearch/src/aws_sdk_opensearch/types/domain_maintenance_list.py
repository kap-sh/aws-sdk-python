"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainMaintenanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_maintenance_details

DomainMaintenanceList: TypeAlias = list[
    "aws_sdk_opensearch.types.domain_maintenance_details.DomainMaintenanceDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainMaintenanceList) -> list:
    import aws_sdk_opensearch.types.domain_maintenance_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearch.types.domain_maintenance_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DomainMaintenanceList:
    import aws_sdk_opensearch.types.domain_maintenance_details

    out: DomainMaintenanceList = []
    for item in data:
        out.append(
            aws_sdk_opensearch.types.domain_maintenance_details.deserialize_json(item)
        )
    return out
