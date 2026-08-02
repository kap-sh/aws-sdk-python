"""Generated from Smithy shape ``com.amazonaws.ec2#EnableRouteServerPropagationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_propagation


class EnableRouteServerPropagationResult(TypedDict, closed=True):
    route_server_propagation: NotRequired[
        "capo_ec2.types.route_server_propagation.RouteServerPropagation"
    ]
    """<p>Information about the enabled route server propagation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableRouteServerPropagationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_propagation" in value:
        import capo_ec2.types.route_server_propagation

        capo_ec2.types.route_server_propagation.serialize_ec2_query(
            value["route_server_propagation"],
            pairs,
            f"{key_prefix}RouteServerPropagation",
        )


def deserialize_ec2_query(el: Element) -> EnableRouteServerPropagationResult:
    out: EnableRouteServerPropagationResult = {}  # type: ignore[typeddict-item]
    child_route_server_propagation = el.find("RouteServerPropagation")
    if child_route_server_propagation is not None:
        import capo_ec2.types.route_server_propagation

        out["route_server_propagation"] = (
            capo_ec2.types.route_server_propagation.deserialize_ec2_query(
                child_route_server_propagation
            )
        )
    return out
