"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListRoute53HealthChecksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.max_results
    import aws_sdk_arc_region_switch.types.next_token
    import aws_sdk_arc_region_switch.types.plan_arn
    import aws_sdk_arc_region_switch.types.route53_hosted_zone_id
    import aws_sdk_arc_region_switch.types.route53_record_name


class ListRoute53HealthChecksRequest(TypedDict, closed=True):
    arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Route 53 health check request.</p>"""
    hosted_zone_id: NotRequired[
        "aws_sdk_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
    ]
    """<p>The hosted zone ID for the health checks.</p>"""
    record_name: NotRequired[
        "aws_sdk_arc_region_switch.types.route53_record_name.Route53RecordName"
    ]
    """<p>The record name for the health checks.</p>"""
    max_results: NotRequired["aws_sdk_arc_region_switch.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_arc_region_switch.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRoute53HealthChecksRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "hosted_zone_id" in value:
        out["hostedZoneId"] = value["hosted_zone_id"]
    if "record_name" in value:
        out["recordName"] = value["record_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRoute53HealthChecksRequest:
    out: ListRoute53HealthChecksRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListRoute53HealthChecksRequest.arn required")
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    if "recordName" in data:
        out["record_name"] = data["recordName"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
