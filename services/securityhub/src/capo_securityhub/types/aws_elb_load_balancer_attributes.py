"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elb_load_balancer_access_log
    import capo_securityhub.types.aws_elb_load_balancer_additional_attribute_list
    import capo_securityhub.types.aws_elb_load_balancer_connection_draining
    import capo_securityhub.types.aws_elb_load_balancer_connection_settings
    import capo_securityhub.types.aws_elb_load_balancer_cross_zone_load_balancing


class AwsElbLoadBalancerAttributes(TypedDict, closed=True):
    access_log: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_access_log.AwsElbLoadBalancerAccessLog"
    ]
    """<p>Information about the access log configuration for the load balancer.</p> <p>If the access log is enabled, the load balancer captures detailed information about all requests. It delivers the information to a specified S3 bucket.</p>"""
    connection_draining: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_connection_draining.AwsElbLoadBalancerConnectionDraining"
    ]
    """<p>Information about the connection draining configuration for the load balancer.</p> <p>If connection draining is enabled, the load balancer allows existing requests to complete before it shifts traffic away from a deregistered or unhealthy instance.</p>"""
    connection_settings: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_connection_settings.AwsElbLoadBalancerConnectionSettings"
    ]
    """<p>Connection settings for the load balancer.</p> <p>If an idle timeout is configured, the load balancer allows connections to remain idle for the specified duration. When a connection is idle, no data is sent over the connection.</p>"""
    cross_zone_load_balancing: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_cross_zone_load_balancing.AwsElbLoadBalancerCrossZoneLoadBalancing"
    ]
    """<p>Cross-zone load balancing settings for the load balancer.</p> <p>If cross-zone load balancing is enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.</p>"""
    additional_attributes: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_additional_attribute_list.AwsElbLoadBalancerAdditionalAttributeList"
    ]
    """<p>Any additional attributes for a load balancer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerAttributes) -> dict:
    out: dict = {}
    if "access_log" in value:
        import capo_securityhub.types.aws_elb_load_balancer_access_log

        out["AccessLog"] = (
            capo_securityhub.types.aws_elb_load_balancer_access_log.serialize_json(
                value["access_log"]
            )
        )
    if "connection_draining" in value:
        import capo_securityhub.types.aws_elb_load_balancer_connection_draining

        out["ConnectionDraining"] = (
            capo_securityhub.types.aws_elb_load_balancer_connection_draining.serialize_json(
                value["connection_draining"]
            )
        )
    if "connection_settings" in value:
        import capo_securityhub.types.aws_elb_load_balancer_connection_settings

        out["ConnectionSettings"] = (
            capo_securityhub.types.aws_elb_load_balancer_connection_settings.serialize_json(
                value["connection_settings"]
            )
        )
    if "cross_zone_load_balancing" in value:
        import capo_securityhub.types.aws_elb_load_balancer_cross_zone_load_balancing

        out["CrossZoneLoadBalancing"] = (
            capo_securityhub.types.aws_elb_load_balancer_cross_zone_load_balancing.serialize_json(
                value["cross_zone_load_balancing"]
            )
        )
    if "additional_attributes" in value:
        import capo_securityhub.types.aws_elb_load_balancer_additional_attribute_list

        out["AdditionalAttributes"] = (
            capo_securityhub.types.aws_elb_load_balancer_additional_attribute_list.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerAttributes:
    out: AwsElbLoadBalancerAttributes = {}  # type: ignore[typeddict-item]
    if "AccessLog" in data:
        import capo_securityhub.types.aws_elb_load_balancer_access_log

        out["access_log"] = (
            capo_securityhub.types.aws_elb_load_balancer_access_log.deserialize_json(
                data["AccessLog"]
            )
        )
    if "ConnectionDraining" in data:
        import capo_securityhub.types.aws_elb_load_balancer_connection_draining

        out["connection_draining"] = (
            capo_securityhub.types.aws_elb_load_balancer_connection_draining.deserialize_json(
                data["ConnectionDraining"]
            )
        )
    if "ConnectionSettings" in data:
        import capo_securityhub.types.aws_elb_load_balancer_connection_settings

        out["connection_settings"] = (
            capo_securityhub.types.aws_elb_load_balancer_connection_settings.deserialize_json(
                data["ConnectionSettings"]
            )
        )
    if "CrossZoneLoadBalancing" in data:
        import capo_securityhub.types.aws_elb_load_balancer_cross_zone_load_balancing

        out["cross_zone_load_balancing"] = (
            capo_securityhub.types.aws_elb_load_balancer_cross_zone_load_balancing.deserialize_json(
                data["CrossZoneLoadBalancing"]
            )
        )
    if "AdditionalAttributes" in data:
        import capo_securityhub.types.aws_elb_load_balancer_additional_attribute_list

        out["additional_attributes"] = (
            capo_securityhub.types.aws_elb_load_balancer_additional_attribute_list.deserialize_json(
                data["AdditionalAttributes"]
            )
        )
    return out
