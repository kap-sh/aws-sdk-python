"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_associations_list


class GetRouteServerAssociationsResult(TypedDict):
    route_server_associations: NotRequired[
        "aws_sdk_ec2.types.route_server_associations_list.RouteServerAssociationsList"
    ]
    """<p>Information about the associations for the specified route server.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetRouteServerAssociationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_associations" in value:
        import aws_sdk_ec2.types.route_server_associations_list

        aws_sdk_ec2.types.route_server_associations_list.serialize_ec2_query(
            value["route_server_associations"],
            pairs,
            f"{prefix}.RouteServerAssociationSet",
        )


def deserialize_ec2_query(el: Element) -> GetRouteServerAssociationsResult:
    out: GetRouteServerAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("RouteServerAssociationSet") is not None:
        import aws_sdk_ec2.types.route_server_associations_list

        out["route_server_associations"] = (
            aws_sdk_ec2.types.route_server_associations_list.deserialize_ec2_query(
                el, "RouteServerAssociationSet"
            )
        )
    return out
