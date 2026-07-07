"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallDomainListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class GetFirewallDomainListRequest(TypedDict, closed=True):
    firewall_domain_list_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the domain list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallDomainListRequest) -> dict:
    out: dict = {}
    out["FirewallDomainListId"] = value["firewall_domain_list_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallDomainListRequest:
    out: GetFirewallDomainListRequest = {}  # type: ignore[typeddict-item]
    if "FirewallDomainListId" in data:
        out["firewall_domain_list_id"] = data["FirewallDomainListId"]
    else:
        raise DeserializationError(
            "GetFirewallDomainListRequest.firewall_domain_list_id required"
        )
    return out
