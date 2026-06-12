"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.account_id
    import aws_sdk_route53resolver.types.resolver_autodefined_reverse_status
    import aws_sdk_route53resolver.types.resource_id


class ResolverConfig(TypedDict):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>ID for the Resolver configuration.</p>"""
    resource_id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the Amazon Virtual Private Cloud VPC or a Route 53 Profile that you're configuring Resolver for.</p>"""
    owner_id: NotRequired["aws_sdk_route53resolver.types.account_id.AccountId"]
    """<p>The owner account ID of the Amazon Virtual Private Cloud VPC.</p>"""
    autodefined_reverse: NotRequired[
        "aws_sdk_route53resolver.types.resolver_autodefined_reverse_status.ResolverAutodefinedReverseStatus"
    ]
    """<p> The status of whether or not the Resolver will create autodefined rules for reverse DNS lookups. This is enabled by default. The status can be one of following:</p> <ul> <li> <p> <b>ENABLING:</b> Autodefined rules for reverse DNS lookups are being enabled but are not complete.</p> </li> <li> <p> <b>ENABLED:</b> Autodefined rules for reverse DNS lookups are enabled.</p> </li> <li> <p> <b>DISABLING:</b> Autodefined rules for reverse DNS lookups are being disabled but are not complete.</p> </li> <li> <p> <b>DISABLED:</b> Autodefined rules for reverse DNS lookups are disabled.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverConfig) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "autodefined_reverse" in value:
        import aws_sdk_route53resolver.types.resolver_autodefined_reverse_status

        out["AutodefinedReverse"] = (
            aws_sdk_route53resolver.types.resolver_autodefined_reverse_status.serialize_aws_json_1_1(
                value["autodefined_reverse"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverConfig:
    out: ResolverConfig = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "AutodefinedReverse" in data:
        import aws_sdk_route53resolver.types.resolver_autodefined_reverse_status

        out["autodefined_reverse"] = (
            aws_sdk_route53resolver.types.resolver_autodefined_reverse_status.deserialize_aws_json_1_1(
                data["AutodefinedReverse"]
            )
        )
    return out
