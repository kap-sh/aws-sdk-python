"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2RuleGroupDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_rules_list
    import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafv2RuleGroupDetails(TypedDict):
    capacity: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p> The web ACL capacity units (WCUs) required for this rule group. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A description of the rule group that helps with identification. </p>"""
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> A unique identifier for the rule group. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the rule group. You cannot change the name of a rule group after you create it. </p>"""
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the entity. </p>"""
    rules: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_rules_list.AwsWafv2RulesList"
    ]
    """<p> The Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>"""
    scope: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Specifies whether the rule group is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an AppSync GraphQL API, or an Amazon Cognito user pool. </p>"""
    visibility_config: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.AwsWafv2VisibilityConfigDetails"
    ]
    """<p> Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2RuleGroupDetails) -> dict:
    out: dict = {}
    if "capacity" in value:
        out["Capacity"] = value["capacity"]
    if "description" in value:
        out["Description"] = value["description"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "rules" in value:
        import aws_sdk_securityhub.types.aws_wafv2_rules_list

        out["Rules"] = aws_sdk_securityhub.types.aws_wafv2_rules_list.serialize_json(
            value["rules"]
        )
    if "scope" in value:
        out["Scope"] = value["scope"]
    if "visibility_config" in value:
        import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details

        out["VisibilityConfig"] = (
            aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.serialize_json(
                value["visibility_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2RuleGroupDetails:
    out: AwsWafv2RuleGroupDetails = {}  # type: ignore[typeddict-item]
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Rules" in data:
        import aws_sdk_securityhub.types.aws_wafv2_rules_list

        out["rules"] = aws_sdk_securityhub.types.aws_wafv2_rules_list.deserialize_json(
            data["Rules"]
        )
    if "Scope" in data:
        out["scope"] = data["Scope"]
    if "VisibilityConfig" in data:
        import aws_sdk_securityhub.types.aws_wafv2_visibility_config_details

        out["visibility_config"] = (
            aws_sdk_securityhub.types.aws_wafv2_visibility_config_details.deserialize_json(
                data["VisibilityConfig"]
            )
        )
    return out
