"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListRoute53HealthChecksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.next_token
    import aws_sdk_arc_region_switch.types.route53_health_check_list


class ListRoute53HealthChecksResponse(TypedDict):
    health_checks: NotRequired[
        "aws_sdk_arc_region_switch.types.route53_health_check_list.Route53HealthCheckList"
    ]
    """<p>List of the health checks requested.</p>"""
    next_token: NotRequired["aws_sdk_arc_region_switch.types.next_token.NextToken"]
    """<p>A pagination token. A response may contain no results while still including a <code>nextToken</code>. Continue paginating until <code>nextToken</code> is null to retrieve all results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRoute53HealthChecksResponse) -> dict:
    out: dict = {}
    if "health_checks" in value:
        import aws_sdk_arc_region_switch.types.route53_health_check_list

        out["healthChecks"] = (
            aws_sdk_arc_region_switch.types.route53_health_check_list.serialize_aws_json_1_0(
                value["health_checks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRoute53HealthChecksResponse:
    out: ListRoute53HealthChecksResponse = {}  # type: ignore[typeddict-item]
    if "healthChecks" in data:
        import aws_sdk_arc_region_switch.types.route53_health_check_list

        out["health_checks"] = (
            aws_sdk_arc_region_switch.types.route53_health_check_list.deserialize_aws_json_1_0(
                data["healthChecks"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
