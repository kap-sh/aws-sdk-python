"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointCidrOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_endpoint_port_range_list
    import capo_ec2.types.verified_access_endpoint_protocol
    import capo_ec2.types.verified_access_endpoint_subnet_id_list


class VerifiedAccessEndpointCidrOptions(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR.</p>"""
    port_ranges: NotRequired[
        "capo_ec2.types.verified_access_endpoint_port_range_list.VerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""
    protocol: NotRequired[
        "capo_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The protocol.</p>"""
    subnet_ids: NotRequired[
        "capo_ec2.types.verified_access_endpoint_subnet_id_list.VerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessEndpointCidrOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "port_ranges" in value:
        import capo_ec2.types.verified_access_endpoint_port_range_list

        capo_ec2.types.verified_access_endpoint_port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{prefix}.PortRangeSet"
        )
    if "protocol" in value:
        import capo_ec2.types.verified_access_endpoint_protocol

        capo_ec2.types.verified_access_endpoint_protocol.serialize_ec2_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "subnet_ids" in value:
        import capo_ec2.types.verified_access_endpoint_subnet_id_list

        capo_ec2.types.verified_access_endpoint_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIdSet"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointCidrOptions:
    out: VerifiedAccessEndpointCidrOptions = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    if el.find("PortRangeSet") is not None:
        import capo_ec2.types.verified_access_endpoint_port_range_list

        out["port_ranges"] = (
            capo_ec2.types.verified_access_endpoint_port_range_list.deserialize_ec2_query(
                el, "PortRangeSet"
            )
        )
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_ec2.types.verified_access_endpoint_protocol

        out["protocol"] = (
            capo_ec2.types.verified_access_endpoint_protocol.deserialize_ec2_query(
                child_protocol
            )
        )
    if el.find("SubnetIdSet") is not None:
        import capo_ec2.types.verified_access_endpoint_subnet_id_list

        out["subnet_ids"] = (
            capo_ec2.types.verified_access_endpoint_subnet_id_list.deserialize_ec2_query(
                el, "SubnetIdSet"
            )
        )
    return out
