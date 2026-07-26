"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Route53HealthCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.route53_health_check_id
    import capo_arc_region_switch.types.route53_health_check_status
    import capo_arc_region_switch.types.route53_hosted_zone_id
    import capo_arc_region_switch.types.route53_record_name


class Route53HealthCheck(TypedDict, closed=True):
    hosted_zone_id: (
        "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
    )
    """<p>The Amazon Route 53 health check hosted zone ID.</p>"""
    record_name: "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
    """<p>The Amazon Route 53 record name.</p>"""
    health_check_id: NotRequired[
        "capo_arc_region_switch.types.route53_health_check_id.Route53HealthCheckId"
    ]
    """<p>The Amazon Route 53 health check ID.</p>"""
    status: NotRequired[
        "capo_arc_region_switch.types.route53_health_check_status.Route53HealthCheckStatus"
    ]
    """<p>The Amazon Route 53 health check status.</p>"""
    region: "capo_arc_region_switch.types.region.Region"
    """<p>The Amazon Route 53 Region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53HealthCheck) -> dict:
    out: dict = {}
    out["hostedZoneId"] = value["hosted_zone_id"]
    out["recordName"] = value["record_name"]
    if "health_check_id" in value:
        out["healthCheckId"] = value["health_check_id"]
    if "status" in value:
        import capo_arc_region_switch.types.route53_health_check_status

        out["status"] = (
            capo_arc_region_switch.types.route53_health_check_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    out["region"] = value["region"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Route53HealthCheck:
    out: Route53HealthCheck = {}  # type: ignore[typeddict-item]
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    else:
        raise DeserializationError("Route53HealthCheck.hosted_zone_id required")
    if "recordName" in data:
        out["record_name"] = data["recordName"]
    else:
        raise DeserializationError("Route53HealthCheck.record_name required")
    if "healthCheckId" in data:
        out["health_check_id"] = data["healthCheckId"]
    if "status" in data:
        import capo_arc_region_switch.types.route53_health_check_status

        out["status"] = (
            capo_arc_region_switch.types.route53_health_check_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("Route53HealthCheck.region required")
    return out
