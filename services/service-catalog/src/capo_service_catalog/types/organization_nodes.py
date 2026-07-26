"""Generated from Smithy shape ``com.amazonaws.servicecatalog#OrganizationNodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.organization_node

OrganizationNodes: TypeAlias = list[
    "capo_service_catalog.types.organization_node.OrganizationNode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationNodes) -> list:
    import capo_service_catalog.types.organization_node

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.organization_node.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationNodes:
    import capo_service_catalog.types.organization_node

    out: OrganizationNodes = []
    for item in data:
        out.append(
            capo_service_catalog.types.organization_node.deserialize_aws_json_1_1(item)
        )
    return out
