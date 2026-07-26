"""Generated from Smithy shape ``com.amazonaws.redshift#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer
    import capo_redshift.types.string
    import capo_redshift.types.vpc_endpoints_list


class Endpoint(TypedDict, closed=True):
    address: NotRequired["capo_redshift.types.string.String"]
    """<p>The DNS address of the Cluster.</p>"""
    port: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The port that the database engine is listening on.</p>"""
    vpc_endpoints: NotRequired[
        "capo_redshift.types.vpc_endpoints_list.VpcEndpointsList"
    ]
    """<p>Describes a connection endpoint.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Endpoint, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "address" in value:
        pairs.append((f"{prefix}.Address", str(value["address"])))
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "vpc_endpoints" in value:
        import capo_redshift.types.vpc_endpoints_list

        capo_redshift.types.vpc_endpoints_list.serialize_query(
            value["vpc_endpoints"], pairs, f"{prefix}.VpcEndpoints"
        )


def deserialize_query(el: Element) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    child_address = el.find("Address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_vpc_endpoints = el.find("VpcEndpoints")
    if child_vpc_endpoints is not None:
        import capo_redshift.types.vpc_endpoints_list

        out["vpc_endpoints"] = capo_redshift.types.vpc_endpoints_list.deserialize_query(
            child_vpc_endpoints
        )
    return out
