"""Generated from Smithy shape ``com.amazonaws.route53domains#GetContactReachabilityStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name
    import aws_sdk_route_53_domains.types.reachability_status


class GetContactReachabilityStatusResponse(TypedDict):
    domain_name: NotRequired["aws_sdk_route_53_domains.types.domain_name.DomainName"]
    """<p>The domain name for which you requested the reachability status.</p>"""
    status: NotRequired[
        "aws_sdk_route_53_domains.types.reachability_status.ReachabilityStatus"
    ]
    """<p>Whether the registrant contact has responded. Values include the following:</p> <dl> <dt>PENDING</dt> <dd> <p>We sent the confirmation email and haven't received a response yet.</p> </dd> <dt>DONE</dt> <dd> <p>We sent the email and got confirmation from the registrant contact.</p> </dd> <dt>EXPIRED</dt> <dd> <p>The time limit expired before the registrant contact responded.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactReachabilityStatusResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "status" in value:
        import aws_sdk_route_53_domains.types.reachability_status

        out["status"] = (
            aws_sdk_route_53_domains.types.reachability_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactReachabilityStatusResponse:
    out: GetContactReachabilityStatusResponse = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "status" in data:
        import aws_sdk_route_53_domains.types.reachability_status

        out["status"] = (
            aws_sdk_route_53_domains.types.reachability_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
