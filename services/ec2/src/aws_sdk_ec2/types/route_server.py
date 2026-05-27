"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
