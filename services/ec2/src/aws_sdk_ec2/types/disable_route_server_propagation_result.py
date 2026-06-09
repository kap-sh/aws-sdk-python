"""Generated from Smithy shape ``com.amazonaws.ec2#DisableRouteServerPropagationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_propagation


class DisableRouteServerPropagationResult(TypedDict):
    route_server_propagation: NotRequired[
        "aws_sdk_ec2.types.route_server_propagation.RouteServerPropagation"
    ]
    """<p>Information about the disabled route server propagation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableRouteServerPropagationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "route_server_propagation" in value:
        import aws_sdk_ec2.types.route_server_propagation

        aws_sdk_ec2.types.route_server_propagation.serialize_ec2_query(
            value["route_server_propagation"], pairs, f"{prefix}.RouteServerPropagation"
        )


def deserialize_ec2_query(el: Element) -> DisableRouteServerPropagationResult:
    out: DisableRouteServerPropagationResult = {}  # type: ignore[typeddict-item]
    child_route_server_propagation = el.find("RouteServerPropagation")
    if child_route_server_propagation is not None:
        import aws_sdk_ec2.types.route_server_propagation

        out["route_server_propagation"] = (
            aws_sdk_ec2.types.route_server_propagation.deserialize_ec2_query(
                child_route_server_propagation
            )
        )
    return out
