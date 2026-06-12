"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.account_id
    import aws_sdk_route53resolver.types.arn
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.share_status


class FirewallRuleGroupMetadata(TypedDict):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the rule group. </p>"""
    arn: NotRequired["aws_sdk_route53resolver.types.arn.Arn"]
    """<p>The ARN (Amazon Resource Name) of the rule group.</p>"""
    name: NotRequired["aws_sdk_route53resolver.types.name.Name"]
    """<p>The name of the rule group.</p>"""
    owner_id: NotRequired["aws_sdk_route53resolver.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the account that created the rule group. When a rule group is shared with your account, this is the account that has shared the rule group with you. </p>"""
    creator_request_id: NotRequired[
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp. </p>"""
    share_status: NotRequired["aws_sdk_route53resolver.types.share_status.ShareStatus"]
    """<p>Whether the rule group is shared with other Amazon Web Services accounts, or was shared with the current account by another Amazon Web Services account. Sharing is configured through Resource Access Manager (RAM).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroupMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "share_status" in value:
        import aws_sdk_route53resolver.types.share_status

        out["ShareStatus"] = (
            aws_sdk_route53resolver.types.share_status.serialize_aws_json_1_1(
                value["share_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRuleGroupMetadata:
    out: FirewallRuleGroupMetadata = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "ShareStatus" in data:
        import aws_sdk_route53resolver.types.share_status

        out["share_status"] = (
            aws_sdk_route53resolver.types.share_status.deserialize_aws_json_1_1(
                data["ShareStatus"]
            )
        )
    return out
