"""Generated from Smithy shape ``com.amazonaws.ec2#CreateClientVpnRouteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_route_status


class CreateClientVpnRouteResult(TypedDict, closed=True):
    status: NotRequired["capo_ec2.types.client_vpn_route_status.ClientVpnRouteStatus"]
    """<p>The current state of the route.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateClientVpnRouteResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        import capo_ec2.types.client_vpn_route_status

        capo_ec2.types.client_vpn_route_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> CreateClientVpnRouteResult:
    out: CreateClientVpnRouteResult = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.client_vpn_route_status

        out["status"] = capo_ec2.types.client_vpn_route_status.deserialize_ec2_query(
            child_status
        )
    return out
