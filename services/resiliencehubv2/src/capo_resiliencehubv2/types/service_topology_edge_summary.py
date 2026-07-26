"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceTopologyEdgeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.edge_property_list


class ServiceTopologyEdgeSummary(TypedDict, closed=True):
    source_resource_identifier: "str"
    """<p>The identifier of the source resource.</p>"""
    destination_resource_identifier: "str"
    """<p>The identifier of the destination resource.</p>"""
    properties: NotRequired[
        "capo_resiliencehubv2.types.edge_property_list.EdgePropertyList"
    ]
    """<p>The properties of the topology edge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceTopologyEdgeSummary) -> dict:
    out: dict = {}
    out["sourceResourceIdentifier"] = value["source_resource_identifier"]
    out["destinationResourceIdentifier"] = value["destination_resource_identifier"]
    if "properties" in value:
        import capo_resiliencehubv2.types.edge_property_list

        out["properties"] = (
            capo_resiliencehubv2.types.edge_property_list.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceTopologyEdgeSummary:
    out: ServiceTopologyEdgeSummary = {}  # type: ignore[typeddict-item]
    if "sourceResourceIdentifier" in data:
        out["source_resource_identifier"] = data["sourceResourceIdentifier"]
    else:
        raise DeserializationError(
            "ServiceTopologyEdgeSummary.source_resource_identifier required"
        )
    if "destinationResourceIdentifier" in data:
        out["destination_resource_identifier"] = data["destinationResourceIdentifier"]
    else:
        raise DeserializationError(
            "ServiceTopologyEdgeSummary.destination_resource_identifier required"
        )
    if "properties" in data:
        import capo_resiliencehubv2.types.edge_property_list

        out["properties"] = (
            capo_resiliencehubv2.types.edge_property_list.deserialize_json(
                data["properties"]
            )
        )
    return out
