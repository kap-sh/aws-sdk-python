"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfaceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_interface
    import capo_ec2.types.string


class CreateNetworkInterfaceResult(TypedDict, closed=True):
    network_interface: NotRequired["capo_ec2.types.network_interface.NetworkInterface"]
    """<p>Information about the network interface.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInterfaceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_interface" in value:
        import capo_ec2.types.network_interface

        capo_ec2.types.network_interface.serialize_ec2_query(
            value["network_interface"], pairs, f"{prefix}.NetworkInterface"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateNetworkInterfaceResult:
    out: CreateNetworkInterfaceResult = {}  # type: ignore[typeddict-item]
    child_network_interface = el.find("NetworkInterface")
    if child_network_interface is not None:
        import capo_ec2.types.network_interface

        out["network_interface"] = (
            capo_ec2.types.network_interface.deserialize_ec2_query(
                child_network_interface
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
