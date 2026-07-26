"""Generated from Smithy shape ``com.amazonaws.redshift#VpcEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.network_interface_list
    import capo_redshift.types.string


class VpcEndpoint(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.</p>"""
    vpc_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The VPC identifier that the endpoint is associated. </p>"""
    network_interfaces: NotRequired[
        "capo_redshift.types.network_interface_list.NetworkInterfaceList"
    ]
    """<p>One or more network interfaces of the endpoint. Also known as an interface endpoint. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VpcEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc_endpoint_id" in value:
        pairs.append((f"{prefix}.VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "network_interfaces" in value:
        import capo_redshift.types.network_interface_list

        capo_redshift.types.network_interface_list.serialize_query(
            value["network_interfaces"], pairs, f"{prefix}.NetworkInterfaces"
        )


def deserialize_query(el: Element) -> VpcEndpoint:
    out: VpcEndpoint = {}  # type: ignore[typeddict-item]
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_network_interfaces = el.find("NetworkInterfaces")
    if child_network_interfaces is not None:
        import capo_redshift.types.network_interface_list

        out["network_interfaces"] = (
            capo_redshift.types.network_interface_list.deserialize_query(
                child_network_interfaces
            )
        )
    return out
