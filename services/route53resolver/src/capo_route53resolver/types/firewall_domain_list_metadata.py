"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainListMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.category
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.domain_list_type
    import capo_route53resolver.types.name
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.service_principle


class FirewallDomainListMetadata(TypedDict, closed=True):
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the domain list. </p>"""
    arn: NotRequired["capo_route53resolver.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the firewall domain list metadata.</p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name of the domain list. </p>"""
    creator_request_id: NotRequired[
        "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp. </p>"""
    managed_owner_name: NotRequired[
        "capo_route53resolver.types.service_principle.ServicePrinciple"
    ]
    """<p>The owner of the list, used only for lists that are not managed by you. For example, the managed domain list <code>AWSManagedDomainsMalwareDomainList</code> has the managed owner name <code>Route 53 Resolver DNS Firewall</code>.</p>"""
    managed_list_type: NotRequired[
        "capo_route53resolver.types.domain_list_type.DomainListType"
    ]
    """<p>The type of the managed domain list, for example <code>THREAT</code>.</p>"""
    category: NotRequired["capo_route53resolver.types.category.Category"]
    """<p>The category of the domain list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDomainListMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "managed_owner_name" in value:
        out["ManagedOwnerName"] = value["managed_owner_name"]
    if "managed_list_type" in value:
        import capo_route53resolver.types.domain_list_type

        out["ManagedListType"] = (
            capo_route53resolver.types.domain_list_type.serialize_aws_json_1_1(
                value["managed_list_type"]
            )
        )
    if "category" in value:
        out["Category"] = value["category"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallDomainListMetadata:
    out: FirewallDomainListMetadata = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "ManagedOwnerName" in data:
        out["managed_owner_name"] = data["ManagedOwnerName"]
    if "ManagedListType" in data:
        import capo_route53resolver.types.domain_list_type

        out["managed_list_type"] = (
            capo_route53resolver.types.domain_list_type.deserialize_aws_json_1_1(
                data["ManagedListType"]
            )
        )
    if "Category" in data:
        out["category"] = data["Category"]
    return out
