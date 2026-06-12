"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DomainDescriptionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.aws_account_id_type
    import aws_sdk_cognito_identity_provider.types.custom_domain_config_type
    import aws_sdk_cognito_identity_provider.types.domain_status_type
    import aws_sdk_cognito_identity_provider.types.domain_type
    import aws_sdk_cognito_identity_provider.types.domain_version_type
    import aws_sdk_cognito_identity_provider.types.routing_type
    import aws_sdk_cognito_identity_provider.types.s3_bucket_type
    import aws_sdk_cognito_identity_provider.types.string_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type
    import aws_sdk_cognito_identity_provider.types.wrapped_integer_type


class DomainDescriptionType(TypedDict):
    user_pool_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that the domain is attached to.</p>"""
    aws_account_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.aws_account_id_type.AWSAccountIdType"
    ]
    """<p>The Amazon Web Services account that you created the user pool in.</p>"""
    domain: NotRequired[
        "aws_sdk_cognito_identity_provider.types.domain_type.DomainType"
    ]
    """<p>The domain string. For custom domains, this is the fully-qualified domain name, such as <code>auth.example.com</code>. For Amazon Cognito prefix domains, this is the prefix alone, such as <code>auth</code>.</p>"""
    s3_bucket: NotRequired[
        "aws_sdk_cognito_identity_provider.types.s3_bucket_type.S3BucketType"
    ]
    """<p>The Amazon S3 bucket where the static files for this domain are stored.</p>"""
    cloud_front_distribution: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The Amazon CloudFront endpoint that hosts your custom domain.</p>"""
    version: NotRequired[
        "aws_sdk_cognito_identity_provider.types.domain_version_type.DomainVersionType"
    ]
    """<p>The app version.</p>"""
    status: NotRequired[
        "aws_sdk_cognito_identity_provider.types.domain_status_type.DomainStatusType"
    ]
    """<p>The domain status.</p>"""
    custom_domain_config: NotRequired[
        "aws_sdk_cognito_identity_provider.types.custom_domain_config_type.CustomDomainConfigType"
    ]
    """<p>The configuration for a custom domain that hosts the sign-up and sign-in webpages for your application.</p>"""
    managed_login_version: NotRequired[
        "aws_sdk_cognito_identity_provider.types.wrapped_integer_type.WrappedIntegerType"
    ]
    """<p>The version of managed login branding that you want to apply to your domain. A value of <code>1</code> indicates hosted UI (classic) branding and a version of <code>2</code> indicates managed login branding.</p> <p>Managed login requires that your user pool be configured for any <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html\">feature plan</a> other than <code>Lite</code>.</p>"""
    routing: NotRequired[
        "aws_sdk_cognito_identity_provider.types.routing_type.RoutingType"
    ]
    """<p>The routing configuration for the domain, including failover settings for multi-region deployments. Currently only <code>Failover</code> configurations are allowed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainDescriptionType) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "aws_account_id" in value:
        out["AWSAccountId"] = value["aws_account_id"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "cloud_front_distribution" in value:
        out["CloudFrontDistribution"] = value["cloud_front_distribution"]
    if "version" in value:
        out["Version"] = value["version"]
    if "status" in value:
        import aws_sdk_cognito_identity_provider.types.domain_status_type

        out["Status"] = (
            aws_sdk_cognito_identity_provider.types.domain_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "custom_domain_config" in value:
        import aws_sdk_cognito_identity_provider.types.custom_domain_config_type

        out["CustomDomainConfig"] = (
            aws_sdk_cognito_identity_provider.types.custom_domain_config_type.serialize_aws_json_1_1(
                value["custom_domain_config"]
            )
        )
    if "managed_login_version" in value:
        out["ManagedLoginVersion"] = value["managed_login_version"]
    if "routing" in value:
        import aws_sdk_cognito_identity_provider.types.routing_type

        out["Routing"] = (
            aws_sdk_cognito_identity_provider.types.routing_type.serialize_aws_json_1_1(
                value["routing"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainDescriptionType:
    out: DomainDescriptionType = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    if "AWSAccountId" in data:
        out["aws_account_id"] = data["AWSAccountId"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    if "CloudFrontDistribution" in data:
        out["cloud_front_distribution"] = data["CloudFrontDistribution"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Status" in data:
        import aws_sdk_cognito_identity_provider.types.domain_status_type

        out["status"] = (
            aws_sdk_cognito_identity_provider.types.domain_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CustomDomainConfig" in data:
        import aws_sdk_cognito_identity_provider.types.custom_domain_config_type

        out["custom_domain_config"] = (
            aws_sdk_cognito_identity_provider.types.custom_domain_config_type.deserialize_aws_json_1_1(
                data["CustomDomainConfig"]
            )
        )
    if "ManagedLoginVersion" in data:
        out["managed_login_version"] = data["ManagedLoginVersion"]
    if "Routing" in data:
        import aws_sdk_cognito_identity_provider.types.routing_type

        out["routing"] = (
            aws_sdk_cognito_identity_provider.types.routing_type.deserialize_aws_json_1_1(
                data["Routing"]
            )
        )
    return out
