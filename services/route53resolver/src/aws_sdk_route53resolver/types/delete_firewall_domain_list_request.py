"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteFirewallDomainListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class DeleteFirewallDomainListRequest(TypedDict):
    firewall_domain_list_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the domain list that you want to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallDomainListRequest) -> dict:
    out: dict = {}
    out["FirewallDomainListId"] = value["firewall_domain_list_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFirewallDomainListRequest:
    out: DeleteFirewallDomainListRequest = {}  # type: ignore[typeddict-item]
    if "FirewallDomainListId" in data:
        out["firewall_domain_list_id"] = data["FirewallDomainListId"]
    else:
        raise DeserializationError(
            "DeleteFirewallDomainListRequest.firewall_domain_list_id required"
        )
    return out
