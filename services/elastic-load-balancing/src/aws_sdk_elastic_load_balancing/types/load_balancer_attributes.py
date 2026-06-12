"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#LoadBalancerAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_log
    import aws_sdk_elastic_load_balancing.types.additional_attributes
    import aws_sdk_elastic_load_balancing.types.connection_draining
    import aws_sdk_elastic_load_balancing.types.connection_settings
    import aws_sdk_elastic_load_balancing.types.cross_zone_load_balancing


class LoadBalancerAttributes(TypedDict):
    cross_zone_load_balancing: NotRequired[
        "aws_sdk_elastic_load_balancing.types.cross_zone_load_balancing.CrossZoneLoadBalancing"
    ]
    """<p>If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html\">Configure Cross-Zone Load Balancing</a> in the <i>Classic Load Balancers Guide</i>.</p>"""
    access_log: NotRequired["aws_sdk_elastic_load_balancing.types.access_log.AccessLog"]
    """<p>If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html\">Enable Access Logs</a> in the <i>Classic Load Balancers Guide</i>.</p>"""
    connection_draining: NotRequired[
        "aws_sdk_elastic_load_balancing.types.connection_draining.ConnectionDraining"
    ]
    """<p>If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html\">Configure Connection Draining</a> in the <i>Classic Load Balancers Guide</i>.</p>"""
    connection_settings: NotRequired[
        "aws_sdk_elastic_load_balancing.types.connection_settings.ConnectionSettings"
    ]
    """<p>If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.</p> <p>By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html\">Configure Idle Connection Timeout</a> in the <i>Classic Load Balancers Guide</i>.</p>"""
    additional_attributes: NotRequired[
        "aws_sdk_elastic_load_balancing.types.additional_attributes.AdditionalAttributes"
    ]
    """<p>Any additional attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cross_zone_load_balancing" in value:
        import aws_sdk_elastic_load_balancing.types.cross_zone_load_balancing

        aws_sdk_elastic_load_balancing.types.cross_zone_load_balancing.serialize_query(
            value["cross_zone_load_balancing"],
            pairs,
            f"{prefix}.CrossZoneLoadBalancing",
        )
    if "access_log" in value:
        import aws_sdk_elastic_load_balancing.types.access_log

        aws_sdk_elastic_load_balancing.types.access_log.serialize_query(
            value["access_log"], pairs, f"{prefix}.AccessLog"
        )
    if "connection_draining" in value:
        import aws_sdk_elastic_load_balancing.types.connection_draining

        aws_sdk_elastic_load_balancing.types.connection_draining.serialize_query(
            value["connection_draining"], pairs, f"{prefix}.ConnectionDraining"
        )
    if "connection_settings" in value:
        import aws_sdk_elastic_load_balancing.types.connection_settings

        aws_sdk_elastic_load_balancing.types.connection_settings.serialize_query(
            value["connection_settings"], pairs, f"{prefix}.ConnectionSettings"
        )
    if "additional_attributes" in value:
        import aws_sdk_elastic_load_balancing.types.additional_attributes

        aws_sdk_elastic_load_balancing.types.additional_attributes.serialize_query(
            value["additional_attributes"], pairs, f"{prefix}.AdditionalAttributes"
        )


def deserialize_query(el: Element) -> LoadBalancerAttributes:
    out: LoadBalancerAttributes = {}  # type: ignore[typeddict-item]
    child_cross_zone_load_balancing = el.find("CrossZoneLoadBalancing")
    if child_cross_zone_load_balancing is not None:
        import aws_sdk_elastic_load_balancing.types.cross_zone_load_balancing

        out["cross_zone_load_balancing"] = (
            aws_sdk_elastic_load_balancing.types.cross_zone_load_balancing.deserialize_query(
                child_cross_zone_load_balancing
            )
        )
    child_access_log = el.find("AccessLog")
    if child_access_log is not None:
        import aws_sdk_elastic_load_balancing.types.access_log

        out["access_log"] = (
            aws_sdk_elastic_load_balancing.types.access_log.deserialize_query(
                child_access_log
            )
        )
    child_connection_draining = el.find("ConnectionDraining")
    if child_connection_draining is not None:
        import aws_sdk_elastic_load_balancing.types.connection_draining

        out["connection_draining"] = (
            aws_sdk_elastic_load_balancing.types.connection_draining.deserialize_query(
                child_connection_draining
            )
        )
    child_connection_settings = el.find("ConnectionSettings")
    if child_connection_settings is not None:
        import aws_sdk_elastic_load_balancing.types.connection_settings

        out["connection_settings"] = (
            aws_sdk_elastic_load_balancing.types.connection_settings.deserialize_query(
                child_connection_settings
            )
        )
    child_additional_attributes = el.find("AdditionalAttributes")
    if child_additional_attributes is not None:
        import aws_sdk_elastic_load_balancing.types.additional_attributes

        out["additional_attributes"] = (
            aws_sdk_elastic_load_balancing.types.additional_attributes.deserialize_query(
                child_additional_attributes
            )
        )
    return out
