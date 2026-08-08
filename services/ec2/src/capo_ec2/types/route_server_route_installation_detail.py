"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRouteInstallationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_route_installation_status
    import capo_ec2.types.route_table_id
    import capo_ec2.types.string


class RouteServerRouteInstallationDetail(TypedDict, closed=True):
    route_table_id: NotRequired["capo_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the route table where the route is being installed.</p>"""
    route_installation_status: NotRequired[
        "capo_ec2.types.route_server_route_installation_status.RouteServerRouteInstallationStatus"
    ]
    """<p>The current installation status of the route in the route table.</p>"""
    route_installation_status_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the current installation status of the route.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerRouteInstallationDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_table_id" in value:
        pairs.append((f"{key_prefix}RouteTableId", str(value["route_table_id"])))
    if "route_installation_status" in value:
        import capo_ec2.types.route_server_route_installation_status

        capo_ec2.types.route_server_route_installation_status.serialize_ec2_query(
            value["route_installation_status"],
            pairs,
            f"{key_prefix}RouteInstallationStatus",
        )
    if "route_installation_status_reason" in value:
        pairs.append(
            (
                f"{key_prefix}RouteInstallationStatusReason",
                str(value["route_installation_status_reason"]),
            )
        )


def deserialize_ec2_query(el: Element) -> RouteServerRouteInstallationDetail:
    out: RouteServerRouteInstallationDetail = {}  # type: ignore[typeddict-item]
    child_route_table_id = el.find("routeTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    child_route_installation_status = el.find("routeInstallationStatus")
    if child_route_installation_status is not None:
        import capo_ec2.types.route_server_route_installation_status

        out["route_installation_status"] = (
            capo_ec2.types.route_server_route_installation_status.deserialize_ec2_query(
                child_route_installation_status
            )
        )
    child_route_installation_status_reason = el.find("routeInstallationStatusReason")
    if child_route_installation_status_reason is not None:
        out["route_installation_status_reason"] = str(
            child_route_installation_status_reason.text or ""
        )
    return out
