"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteClientVpnEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint_status


class DeleteClientVpnEndpointResult(TypedDict):
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_status.ClientVpnEndpointStatus"
    ]
    """<p>The current state of the Client VPN endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteClientVpnEndpointResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        import aws_sdk_ec2.types.client_vpn_endpoint_status

        aws_sdk_ec2.types.client_vpn_endpoint_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> DeleteClientVpnEndpointResult:
    out: DeleteClientVpnEndpointResult = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.client_vpn_endpoint_status

        out["status"] = (
            aws_sdk_ec2.types.client_vpn_endpoint_status.deserialize_ec2_query(
                child_status
            )
        )
    return out
