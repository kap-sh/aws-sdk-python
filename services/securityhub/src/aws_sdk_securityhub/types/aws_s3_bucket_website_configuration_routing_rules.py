"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketWebsiteConfigurationRoutingRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_website_configuration_routing_rule

AwsS3BucketWebsiteConfigurationRoutingRules: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_s3_bucket_website_configuration_routing_rule.AwsS3BucketWebsiteConfigurationRoutingRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketWebsiteConfigurationRoutingRules) -> list:
    import aws_sdk_securityhub.types.aws_s3_bucket_website_configuration_routing_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_s3_bucket_website_configuration_routing_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsS3BucketWebsiteConfigurationRoutingRules:
    import aws_sdk_securityhub.types.aws_s3_bucket_website_configuration_routing_rule

    out: AwsS3BucketWebsiteConfigurationRoutingRules = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_s3_bucket_website_configuration_routing_rule.deserialize_json(
                item
            )
        )
    return out
