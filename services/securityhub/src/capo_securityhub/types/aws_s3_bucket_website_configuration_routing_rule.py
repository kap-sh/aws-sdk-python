"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketWebsiteConfigurationRoutingRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_condition
    import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_redirect


class AwsS3BucketWebsiteConfigurationRoutingRule(TypedDict, closed=True):
    condition: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_condition.AwsS3BucketWebsiteConfigurationRoutingRuleCondition"
    ]
    """<p>Provides the condition that must be met in order to apply the routing rule.</p>"""
    redirect: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_redirect.AwsS3BucketWebsiteConfigurationRoutingRuleRedirect"
    ]
    """<p>Provides the rules to redirect the request if the condition in <code>Condition</code> is met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketWebsiteConfigurationRoutingRule) -> dict:
    out: dict = {}
    if "condition" in value:
        import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_condition

        out["Condition"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_condition.serialize_json(
                value["condition"]
            )
        )
    if "redirect" in value:
        import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_redirect

        out["Redirect"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_redirect.serialize_json(
                value["redirect"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketWebsiteConfigurationRoutingRule:
    out: AwsS3BucketWebsiteConfigurationRoutingRule = {}  # type: ignore[typeddict-item]
    if "Condition" in data:
        import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_condition

        out["condition"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_condition.deserialize_json(
                data["Condition"]
            )
        )
    if "Redirect" in data:
        import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_redirect

        out["redirect"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rule_redirect.deserialize_json(
                data["Redirect"]
            )
        )
    return out
