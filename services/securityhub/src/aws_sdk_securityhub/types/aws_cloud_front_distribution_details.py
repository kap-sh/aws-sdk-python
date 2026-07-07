"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behaviors
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_default_cache_behavior
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_logging
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_origins
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_viewer_certificate
    import aws_sdk_securityhub.types.non_empty_string


class AwsCloudFrontDistributionDetails(TypedDict, closed=True):
    cache_behaviors: NotRequired[
        "aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behaviors.AwsCloudFrontDistributionCacheBehaviors"
    ]
    """<p>Provides information about the cache configuration for the distribution.</p>"""
    default_cache_behavior: NotRequired[
        "aws_sdk_securityhub.types.aws_cloud_front_distribution_default_cache_behavior.AwsCloudFrontDistributionDefaultCacheBehavior"
    ]
    """<p>The default cache behavior for the configuration.</p>"""
    default_root_object: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The object that CloudFront sends in response to requests from the origin (for example, index.html) when a viewer requests the root URL for the distribution (http://www.example.com) instead of an object in your distribution (http://www.example.com/product-description.html). </p>"""
    domain_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The domain name corresponding to the distribution.</p>"""
    e_tag: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The entity tag is a hash of the object.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when that the distribution was last modified.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    logging: NotRequired[
        "aws_sdk_securityhub.types.aws_cloud_front_distribution_logging.AwsCloudFrontDistributionLogging"
    ]
    """<p>A complex type that controls whether access logs are written for the distribution.</p>"""
    origins: NotRequired[
        "aws_sdk_securityhub.types.aws_cloud_front_distribution_origins.AwsCloudFrontDistributionOrigins"
    ]
    """<p>A complex type that contains information about origins for this distribution.</p>"""
    origin_groups: NotRequired[
        "aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups.AwsCloudFrontDistributionOriginGroups"
    ]
    """<p>Provides information about the origin groups in the distribution.</p>"""
    viewer_certificate: NotRequired[
        "aws_sdk_securityhub.types.aws_cloud_front_distribution_viewer_certificate.AwsCloudFrontDistributionViewerCertificate"
    ]
    """<p>Provides information about the TLS/SSL configuration that the distribution uses to communicate with viewers.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates the current status of the distribution.</p>"""
    web_acl_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A unique identifier that specifies the WAF web ACL, if any, to associate with this distribution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionDetails) -> dict:
    out: dict = {}
    if "cache_behaviors" in value:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behaviors

        out["CacheBehaviors"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behaviors.serialize_json(
                value["cache_behaviors"]
            )
        )
    if "default_cache_behavior" in value:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_default_cache_behavior

        out["DefaultCacheBehavior"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_default_cache_behavior.serialize_json(
                value["default_cache_behavior"]
            )
        )
    if "default_root_object" in value:
        out["DefaultRootObject"] = value["default_root_object"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "last_modified_time" in value:
        out["LastModifiedTime"] = value["last_modified_time"]
    if "logging" in value:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_logging

        out["Logging"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_logging.serialize_json(
                value["logging"]
            )
        )
    if "origins" in value:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_origins

        out["Origins"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origins.serialize_json(
                value["origins"]
            )
        )
    if "origin_groups" in value:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups

        out["OriginGroups"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups.serialize_json(
                value["origin_groups"]
            )
        )
    if "viewer_certificate" in value:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_viewer_certificate

        out["ViewerCertificate"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_viewer_certificate.serialize_json(
                value["viewer_certificate"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "web_acl_id" in value:
        out["WebAclId"] = value["web_acl_id"]
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionDetails:
    out: AwsCloudFrontDistributionDetails = {}  # type: ignore[typeddict-item]
    if "CacheBehaviors" in data:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behaviors

        out["cache_behaviors"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_cache_behaviors.deserialize_json(
                data["CacheBehaviors"]
            )
        )
    if "DefaultCacheBehavior" in data:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_default_cache_behavior

        out["default_cache_behavior"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_default_cache_behavior.deserialize_json(
                data["DefaultCacheBehavior"]
            )
        )
    if "DefaultRootObject" in data:
        out["default_root_object"] = data["DefaultRootObject"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "LastModifiedTime" in data:
        out["last_modified_time"] = data["LastModifiedTime"]
    if "Logging" in data:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_logging

        out["logging"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_logging.deserialize_json(
                data["Logging"]
            )
        )
    if "Origins" in data:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_origins

        out["origins"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origins.deserialize_json(
                data["Origins"]
            )
        )
    if "OriginGroups" in data:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups

        out["origin_groups"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups.deserialize_json(
                data["OriginGroups"]
            )
        )
    if "ViewerCertificate" in data:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_viewer_certificate

        out["viewer_certificate"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_viewer_certificate.deserialize_json(
                data["ViewerCertificate"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "WebAclId" in data:
        out["web_acl_id"] = data["WebAclId"]
    return out
