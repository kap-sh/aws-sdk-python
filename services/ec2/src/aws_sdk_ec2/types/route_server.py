"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_long
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.route_server_id
    import aws_sdk_ec2.types.route_server_persist_routes_state
    import aws_sdk_ec2.types.route_server_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class RouteServer(TypedDict):
    route_server_id: NotRequired["aws_sdk_ec2.types.route_server_id.RouteServerId"]
    """<p>The unique identifier of the route server.</p>"""
    amazon_side_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The Border Gateway Protocol (BGP) Autonomous System Number (ASN) for the appliance. Valid values are from 1 to 4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.</p>"""
    state: NotRequired["aws_sdk_ec2.types.route_server_state.RouteServerState"]
    """<p>The current state of the route server.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route server.</p>"""
    persist_routes_state: NotRequired[
        "aws_sdk_ec2.types.route_server_persist_routes_state.RouteServerPersistRoutesState"
    ]
    """<p>The current state of route persistence for the route server.</p>"""
    persist_routes_duration: NotRequired["aws_sdk_ec2.types.boxed_long.BoxedLong"]
    """<p>The number of minutes a route server will wait after BGP is re-established to unpersist the routes in the FIB and RIB. Value must be in the range of 1-5. The default value is 1. Only valid if <code>persistRoutesState</code> is 'enabled'.</p> <p>If you set the duration to 1 minute, then when your network appliance re-establishes BGP with route server, it has 1 minute to relearn it's adjacent network and advertise those routes to route server before route server resumes normal functionality. In most cases, 1 minute is probably sufficient. If, however, you have concerns that your BGP network may not be capable of fully re-establishing and re-learning everything in 1 minute, you can increase the duration up to 5 minutes.</p>"""
    sns_notifications_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether SNS notifications are enabled for the route server. Enabling SNS notifications persists BGP status changes to an SNS topic provisioned by Amazon Web Services.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the SNS topic where notifications are published.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_id" in value:
        pairs.append((f"{prefix}.RouteServerId", str(value["route_server_id"])))
    if "amazon_side_asn" in value:
        pairs.append((f"{prefix}.AmazonSideAsn", str(value["amazon_side_asn"])))
    if "state" in value:
        import aws_sdk_ec2.types.route_server_state

        aws_sdk_ec2.types.route_server_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "persist_routes_state" in value:
        import aws_sdk_ec2.types.route_server_persist_routes_state

        aws_sdk_ec2.types.route_server_persist_routes_state.serialize_ec2_query(
            value["persist_routes_state"], pairs, f"{prefix}.PersistRoutesState"
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
    if "sns_topic_arn" in value:
        pairs.append((f"{prefix}.SnsTopicArn", str(value["sns_topic_arn"])))


def deserialize_ec2_query(el: Element) -> RouteServer:
    out: RouteServer = {}  # type: ignore[typeddict-item]
    child_route_server_id = el.find("RouteServerId")
    if child_route_server_id is not None:
        out["route_server_id"] = str(child_route_server_id.text or "")
    child_amazon_side_asn = el.find("AmazonSideAsn")
    if child_amazon_side_asn is not None:
        out["amazon_side_asn"] = int(child_amazon_side_asn.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.route_server_state

        out["state"] = aws_sdk_ec2.types.route_server_state.deserialize_ec2_query(
            child_state
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_persist_routes_state = el.find("PersistRoutesState")
    if child_persist_routes_state is not None:
        import aws_sdk_ec2.types.route_server_persist_routes_state

        out["persist_routes_state"] = (
            aws_sdk_ec2.types.route_server_persist_routes_state.deserialize_ec2_query(
                child_persist_routes_state
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
    child_sns_topic_arn = el.find("SnsTopicArn")
    if child_sns_topic_arn is not None:
        out["sns_topic_arn"] = str(child_sns_topic_arn.text or "")
    return out
