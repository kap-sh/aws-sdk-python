"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_long
    import capo_ec2.types.long
    import capo_ec2.types.route_server_persist_routes_action
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateRouteServerRequest(TypedDict, closed=True):
    amazon_side_asn: NotRequired["capo_ec2.types.long.Long"]
    """<p>The private Autonomous System Number (ASN) for the Amazon side of the BGP session. Valid values are from 1 to 4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    persist_routes: NotRequired[
        "capo_ec2.types.route_server_persist_routes_action.RouteServerPersistRoutesAction"
    ]
    """<p>Indicates whether routes should be persisted after all BGP sessions are terminated.</p>"""
    persist_routes_duration: NotRequired["capo_ec2.types.boxed_long.BoxedLong"]
    """<p>The number of minutes a route server will wait after BGP is re-established to unpersist the routes in the FIB and RIB. Value must be in the range of 1-5. Required if PersistRoutes is <code>enabled</code>.</p> <p>If you set the duration to 1 minute, then when your network appliance re-establishes BGP with route server, it has 1 minute to relearn it's adjacent network and advertise those routes to route server before route server resumes normal functionality. In most cases, 1 minute is probably sufficient. If, however, you have concerns that your BGP network may not be capable of fully re-establishing and re-learning everything in 1 minute, you can increase the duration up to 5 minutes.</p>"""
    sns_notifications_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether SNS notifications should be enabled for route server events. Enabling SNS notifications persists BGP status changes to an SNS topic provisioned by Amazon Web Services.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the route server during creation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateRouteServerRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "amazon_side_asn" in value:
        pairs.append((f"{prefix}.AmazonSideAsn", str(value["amazon_side_asn"])))
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "persist_routes" in value:
        import capo_ec2.types.route_server_persist_routes_action

        capo_ec2.types.route_server_persist_routes_action.serialize_ec2_query(
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
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateRouteServerRequest:
    out: CreateRouteServerRequest = {}  # type: ignore[typeddict-item]
    child_amazon_side_asn = el.find("AmazonSideAsn")
    if child_amazon_side_asn is not None:
        out["amazon_side_asn"] = int(child_amazon_side_asn.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_persist_routes = el.find("PersistRoutes")
    if child_persist_routes is not None:
        import capo_ec2.types.route_server_persist_routes_action

        out["persist_routes"] = (
            capo_ec2.types.route_server_persist_routes_action.deserialize_ec2_query(
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
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
