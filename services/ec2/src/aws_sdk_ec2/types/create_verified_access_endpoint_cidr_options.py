"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointCidrOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list
    import aws_sdk_ec2.types.create_verified_access_endpoint_subnet_id_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_protocol


class CreateVerifiedAccessEndpointCidrOptions(TypedDict):
    protocol: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The protocol.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_subnet_id_list.CreateVerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR.</p>"""
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list.CreateVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessEndpointCidrOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "protocol" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_protocol

        aws_sdk_ec2.types.verified_access_endpoint_protocol.serialize_ec2_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "subnet_ids" in value:
        import aws_sdk_ec2.types.create_verified_access_endpoint_subnet_id_list

        aws_sdk_ec2.types.create_verified_access_endpoint_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "port_ranges" in value:
        import aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list

        aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{prefix}.PortRanges"
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessEndpointCidrOptions:
    out: CreateVerifiedAccessEndpointCidrOptions = {}  # type: ignore[typeddict-item]
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_protocol

        out["protocol"] = (
            aws_sdk_ec2.types.verified_access_endpoint_protocol.deserialize_ec2_query(
                child_protocol
            )
        )
    if el.find("SubnetIds") is not None:
        import aws_sdk_ec2.types.create_verified_access_endpoint_subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_ec2.types.create_verified_access_endpoint_subnet_id_list.deserialize_ec2_query(
                el, "SubnetIds"
            )
        )
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    if el.find("PortRanges") is not None:
        import aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list

        out["port_ranges"] = (
            aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list.deserialize_ec2_query(
                el, "PortRanges"
            )
        )
    return out
