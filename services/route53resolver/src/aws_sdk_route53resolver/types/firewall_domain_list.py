"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.arn
    import aws_sdk_route53resolver.types.category
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.domain_list_type
    import aws_sdk_route53resolver.types.firewall_domain_list_status
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.rfc3339_time_string
    import aws_sdk_route53resolver.types.service_principle
    import aws_sdk_route53resolver.types.status_message
    import aws_sdk_route53resolver.types.unsigned


class FirewallDomainList(TypedDict, closed=True):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the domain list. </p>"""
    arn: NotRequired["aws_sdk_route53resolver.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the firewall domain list.</p>"""
    name: NotRequired["aws_sdk_route53resolver.types.name.Name"]
    """<p>The name of the domain list. </p>"""
    domain_count: NotRequired["aws_sdk_route53resolver.types.unsigned.Unsigned"]
    """<p>The number of domain names that are specified in the domain list.</p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.firewall_domain_list_status.FirewallDomainListStatus"
    ]
    """<p>The status of the domain list. </p>"""
    status_message: NotRequired[
        "aws_sdk_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>Additional information about the status of the list, if available.</p>"""
    managed_owner_name: NotRequired[
        "aws_sdk_route53resolver.types.service_principle.ServicePrinciple"
    ]
    """<p>The owner of the list, used only for lists that are not managed by you. For example, the managed domain list <code>AWSManagedDomainsMalwareDomainList</code> has the managed owner name <code>Route 53 Resolver DNS Firewall</code>.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp. </p>"""
    creation_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the domain list was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the domain list was last modified, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    category: NotRequired["aws_sdk_route53resolver.types.category.Category"]
    """<p>The category of the domain list.</p>"""
    managed_list_type: NotRequired[
        "aws_sdk_route53resolver.types.domain_list_type.DomainListType"
    ]
    """<p>The type of the managed domain list, for example <code>THREAT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDomainList) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "domain_count" in value:
        out["DomainCount"] = value["domain_count"]
    if "status" in value:
        import aws_sdk_route53resolver.types.firewall_domain_list_status

        out["Status"] = (
            aws_sdk_route53resolver.types.firewall_domain_list_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "managed_owner_name" in value:
        out["ManagedOwnerName"] = value["managed_owner_name"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    if "category" in value:
        out["Category"] = value["category"]
    if "managed_list_type" in value:
        import aws_sdk_route53resolver.types.domain_list_type

        out["ManagedListType"] = (
            aws_sdk_route53resolver.types.domain_list_type.serialize_aws_json_1_1(
                value["managed_list_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallDomainList:
    out: FirewallDomainList = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DomainCount" in data:
        out["domain_count"] = data["DomainCount"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.firewall_domain_list_status

        out["status"] = (
            aws_sdk_route53resolver.types.firewall_domain_list_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "ManagedOwnerName" in data:
        out["managed_owner_name"] = data["ManagedOwnerName"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "ModificationTime" in data:
        out["modification_time"] = data["ModificationTime"]
    if "Category" in data:
        out["category"] = data["Category"]
    if "ManagedListType" in data:
        import aws_sdk_route53resolver.types.domain_list_type

        out["managed_list_type"] = (
            aws_sdk_route53resolver.types.domain_list_type.deserialize_aws_json_1_1(
                data["ManagedListType"]
            )
        )
    return out
