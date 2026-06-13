"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Route53HealthCheckConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.iam_role_arn
    import aws_sdk_arc_region_switch.types.route53_hosted_zone_id
    import aws_sdk_arc_region_switch.types.route53_record_name
    import aws_sdk_arc_region_switch.types.route53_resource_record_set_list


class Route53HealthCheckConfiguration(TypedDict):
    timeout_minutes: "int"
    """<p>The Amazon Route 53 health check configuration time out (in minutes).</p>"""
    cross_account_role: NotRequired[
        "aws_sdk_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    hosted_zone_id: (
        "aws_sdk_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
    )
    """<p>The Amazon Route 53 health check configuration hosted zone ID.</p>"""
    record_name: "aws_sdk_arc_region_switch.types.route53_record_name.Route53RecordName"
    """<p>The Amazon Route 53 health check configuration record name.</p>"""
    record_sets: NotRequired[
        "aws_sdk_arc_region_switch.types.route53_resource_record_set_list.Route53ResourceRecordSetList"
    ]
    """<p>The Amazon Route 53 health check configuration record sets.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53HealthCheckConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["hostedZoneId"] = value["hosted_zone_id"]
    out["recordName"] = value["record_name"]
    if "record_sets" in value:
        import aws_sdk_arc_region_switch.types.route53_resource_record_set_list

        out["recordSets"] = (
            aws_sdk_arc_region_switch.types.route53_resource_record_set_list.serialize_aws_json_1_0(
                value["record_sets"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Route53HealthCheckConfiguration:
    out: Route53HealthCheckConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if "crossAccountRole" in data:
        out["cross_account_role"] = data["crossAccountRole"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    else:
        raise DeserializationError(
            "Route53HealthCheckConfiguration.hosted_zone_id required"
        )
    if "recordName" in data:
        out["record_name"] = data["recordName"]
    else:
        raise DeserializationError(
            "Route53HealthCheckConfiguration.record_name required"
        )
    if "recordSets" in data:
        import aws_sdk_arc_region_switch.types.route53_resource_record_set_list

        out["record_sets"] = (
            aws_sdk_arc_region_switch.types.route53_resource_record_set_list.deserialize_aws_json_1_0(
                data["recordSets"]
            )
        )
    return out
