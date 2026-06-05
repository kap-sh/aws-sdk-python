"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateRouteServerResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_association


class DisassociateRouteServerResult(TypedDict):
    route_server_association: NotRequired[
        "aws_sdk_ec2.types.route_server_association.RouteServerAssociation"
    ]
    """<p>Information about the disassociated route server.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateRouteServerResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_association" in value:
        import aws_sdk_ec2.types.route_server_association

        aws_sdk_ec2.types.route_server_association.serialize_ec2_query(
            value["route_server_association"], pairs, f"{prefix}.RouteServerAssociation"
        )


def deserialize_ec2_query(el: Element) -> DisassociateRouteServerResult:
    out: DisassociateRouteServerResult = {}  # type: ignore[typeddict-item]
    child_route_server_association = el.find("RouteServerAssociation")
    if child_route_server_association is not None:
        import aws_sdk_ec2.types.route_server_association

        out["route_server_association"] = (
            aws_sdk_ec2.types.route_server_association.deserialize_ec2_query(
                child_route_server_association
            )
        )
    return out
