"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyRouteServerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_long
    import aws_sdk_ec2.types.route_server_id
    import aws_sdk_ec2.types.route_server_persist_routes_action


class ModifyRouteServerRequest(TypedDict):
    route_server_id: NotRequired["aws_sdk_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server to modify.</p>"""
    persist_routes: NotRequired[
        "aws_sdk_ec2.types.route_server_persist_routes_action.RouteServerPersistRoutesAction"
    ]
    """<p>Specifies whether to persist routes after all BGP sessions are terminated.</p> <ul> <li> <p>enable: Routes will be persisted in FIB and RIB after all BGP sessions are terminated.</p> </li> <li> <p>disable: Routes will not be persisted in FIB and RIB after all BGP sessions are terminated.</p> </li> <li> <p>reset: If a route server has persisted routes due to all BGP sessions having ended, reset will withdraw all routes and reset route server to an empty FIB and RIB.</p> </li> </ul>"""
    persist_routes_duration: NotRequired["aws_sdk_ec2.types.boxed_long.BoxedLong"]
    """<p>The number of minutes a route server will wait after BGP is re-established to unpersist the routes in the FIB and RIB. Value must be in the range of 1-5. Required if PersistRoutes is <code>enabled</code>.</p> <p>If you set the duration to 1 minute, then when your network appliance re-establishes BGP with route server, it has 1 minute to relearn it's adjacent network and advertise those routes to route server before route server resumes normal functionality. In most cases, 1 minute is probably sufficient. If, however, you have concerns that your BGP network may not be capable of fully re-establishing and re-learning everything in 1 minute, you can increase the duration up to 5 minutes.</p>"""
    sns_notifications_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to enable SNS notifications for route server events. Enabling SNS notifications persists BGP status changes to an SNS topic provisioned by Amazon Web Services.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyRouteServerRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_id" in value:
        pairs.append((f"{prefix}.RouteServerId", str(value["route_server_id"])))
    if "persist_routes" in value:
        import aws_sdk_ec2.types.route_server_persist_routes_action

        aws_sdk_ec2.types.route_server_persist_routes_action.serialize_ec2_query(
            value["persist_routes"], pairs, f"{prefix}.PersistRoutes"
        )
    if "persist_routes_duration" in value:
        pairs.append(
            (f"{prefix}.PersistRoutesDuration", str(value["persist_routes_duration"]))
        )
    if "sns_notifications_enabled" in value:
        pairs.append(
            (
                f"{prefix}.SnsNotificationsEnabled",
                "true" if value["sns_notifications_enabled"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyRouteServerRequest:
    out: ModifyRouteServerRequest = {}  # type: ignore[typeddict-item]
    child_route_server_id = el.find("RouteServerId")
    if child_route_server_id is not None:
        out["route_server_id"] = str(child_route_server_id.text or "")
    child_persist_routes = el.find("PersistRoutes")
    if child_persist_routes is not None:
        import aws_sdk_ec2.types.route_server_persist_routes_action

        out["persist_routes"] = (
            aws_sdk_ec2.types.route_server_persist_routes_action.deserialize_ec2_query(
                child_persist_routes
            )
        )
    child_persist_routes_duration = el.find("PersistRoutesDuration")
    if child_persist_routes_duration is not None:
        out["persist_routes_duration"] = int(child_persist_routes_duration.text or "")
    child_sns_notifications_enabled = el.find("SnsNotificationsEnabled")
    if child_sns_notifications_enabled is not None:
        out["sns_notifications_enabled"] = (
            child_sns_notifications_enabled.text or ""
        ).lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
