"""Generated from Smithy shape ``com.amazonaws.servicecatalog#OrganizationNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.organization_node_type
    import capo_service_catalog.types.organization_node_value


class OrganizationNode(TypedDict, closed=True):
    type: NotRequired[
        "capo_service_catalog.types.organization_node_type.OrganizationNodeType"
    ]
    """<p>The organization node type.</p>"""
    value: NotRequired[
        "capo_service_catalog.types.organization_node_value.OrganizationNodeValue"
    ]
    """<p>The identifier of the organization node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationNode) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_service_catalog.types.organization_node_type

        out["Type"] = (
            capo_service_catalog.types.organization_node_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationNode:
    out: OrganizationNode = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_service_catalog.types.organization_node_type

        out["type"] = (
            capo_service_catalog.types.organization_node_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
