"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_network_arn
    import capo_vpc_lattice.types.service_network_id
    import capo_vpc_lattice.types.service_network_name
    import capo_vpc_lattice.types.timestamp


class ServiceNetworkSummary(TypedDict, closed=True):
    id: NotRequired["capo_vpc_lattice.types.service_network_id.ServiceNetworkId"]
    """<p>The ID of the service network.</p>"""
    name: NotRequired["capo_vpc_lattice.types.service_network_name.ServiceNetworkName"]
    """<p>The name of the service network.</p>"""
    arn: NotRequired["capo_vpc_lattice.types.service_network_arn.ServiceNetworkArn"]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the service network was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the service network was last updated, in ISO-8601 format.</p>"""
    number_of_associated_vp_cs: NotRequired["int"]
    """<p>The number of VPCs associated with the service network.</p>"""
    number_of_associated_services: NotRequired["int"]
    """<p>The number of services associated with the service network.</p>"""
    number_of_associated_resource_configurations: NotRequired["int"]
    """<p>The number of resource configurations associated with a service network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "number_of_associated_vp_cs" in value:
        out["numberOfAssociatedVPCs"] = value["number_of_associated_vp_cs"]
    if "number_of_associated_services" in value:
        out["numberOfAssociatedServices"] = value["number_of_associated_services"]
    if "number_of_associated_resource_configurations" in value:
        out["numberOfAssociatedResourceConfigurations"] = value[
            "number_of_associated_resource_configurations"
        ]
    return out


def deserialize_json(data: dict) -> ServiceNetworkSummary:
    out: ServiceNetworkSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "numberOfAssociatedVPCs" in data:
        out["number_of_associated_vp_cs"] = data["numberOfAssociatedVPCs"]
    if "numberOfAssociatedServices" in data:
        out["number_of_associated_services"] = data["numberOfAssociatedServices"]
    if "numberOfAssociatedResourceConfigurations" in data:
        out["number_of_associated_resource_configurations"] = data[
            "numberOfAssociatedResourceConfigurations"
        ]
    return out
