"""Generated from Smithy shape ``com.amazonaws.rds#RdsCustomClusterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.replica_mode
    import capo_rds.types.string


class RdsCustomClusterConfiguration(TypedDict, closed=True):
    interconnect_subnet_id: NotRequired["capo_rds.types.string.String"]
    """<p>Reserved for future use.</p>"""
    transit_gateway_multicast_domain_id: NotRequired["capo_rds.types.string.String"]
    """<p>Reserved for future use.</p>"""
    replica_mode: NotRequired["capo_rds.types.replica_mode.ReplicaMode"]
    """<p>Reserved for future use.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RdsCustomClusterConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "interconnect_subnet_id" in value:
        pairs.append(
            (f"{prefix}.InterconnectSubnetId", str(value["interconnect_subnet_id"]))
        )
    if "transit_gateway_multicast_domain_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayMulticastDomainId",
                str(value["transit_gateway_multicast_domain_id"]),
            )
        )
    if "replica_mode" in value:
        import capo_rds.types.replica_mode

        capo_rds.types.replica_mode.serialize_query(
            value["replica_mode"], pairs, f"{prefix}.ReplicaMode"
        )


def deserialize_query(el: Element) -> RdsCustomClusterConfiguration:
    out: RdsCustomClusterConfiguration = {}  # type: ignore[typeddict-item]
    child_interconnect_subnet_id = el.find("InterconnectSubnetId")
    if child_interconnect_subnet_id is not None:
        out["interconnect_subnet_id"] = str(child_interconnect_subnet_id.text or "")
    child_transit_gateway_multicast_domain_id = el.find(
        "TransitGatewayMulticastDomainId"
    )
    if child_transit_gateway_multicast_domain_id is not None:
        out["transit_gateway_multicast_domain_id"] = str(
            child_transit_gateway_multicast_domain_id.text or ""
        )
    child_replica_mode = el.find("ReplicaMode")
    if child_replica_mode is not None:
        import capo_rds.types.replica_mode

        out["replica_mode"] = capo_rds.types.replica_mode.deserialize_query(
            child_replica_mode
        )
    return out
