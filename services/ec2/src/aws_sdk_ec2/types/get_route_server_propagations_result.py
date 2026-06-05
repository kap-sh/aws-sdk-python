"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerPropagationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_propagations_list


class GetRouteServerPropagationsResult(TypedDict):
    route_server_propagations: NotRequired[
        "aws_sdk_ec2.types.route_server_propagations_list.RouteServerPropagationsList"
    ]
    """<p>Information about the route propagations for the specified route server.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetRouteServerPropagationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_propagations" in value:
        import aws_sdk_ec2.types.route_server_propagations_list

        aws_sdk_ec2.types.route_server_propagations_list.serialize_ec2_query(
            value["route_server_propagations"],
            pairs,
            f"{prefix}.RouteServerPropagationSet",
        )


def deserialize_ec2_query(el: Element) -> GetRouteServerPropagationsResult:
    out: GetRouteServerPropagationsResult = {}  # type: ignore[typeddict-item]
    if el.find("RouteServerPropagationSet") is not None:
        import aws_sdk_ec2.types.route_server_propagations_list

        out["route_server_propagations"] = (
            aws_sdk_ec2.types.route_server_propagations_list.deserialize_ec2_query(
                el, "RouteServerPropagationSet"
            )
        )
    return out
