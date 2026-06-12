"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.cache_behavior
    import aws_sdk_lightsail.types.cache_behavior_list
    import aws_sdk_lightsail.types.cache_settings
    import aws_sdk_lightsail.types.input_origin
    import aws_sdk_lightsail.types.ip_address_type
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.tag_list
    import aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum


class CreateDistributionRequest(TypedDict):
    distribution_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name for the distribution.</p>"""
    origin: "aws_sdk_lightsail.types.input_origin.InputOrigin"
    """<p>An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.</p> <p>The distribution pulls, caches, and serves content from the origin.</p>"""
    default_cache_behavior: "aws_sdk_lightsail.types.cache_behavior.CacheBehavior"
    """<p>An object that describes the default cache behavior for the distribution.</p>"""
    cache_behavior_settings: NotRequired[
        "aws_sdk_lightsail.types.cache_settings.CacheSettings"
    ]
    """<p>An object that describes the cache behavior settings for the distribution.</p>"""
    cache_behaviors: NotRequired[
        "aws_sdk_lightsail.types.cache_behavior_list.CacheBehaviorList"
    ]
    """<p>An array of objects that describe the per-path cache behavior for the distribution.</p>"""
    bundle_id: "aws_sdk_lightsail.types.string.string"
    """<p>The bundle ID to use for the distribution.</p> <p>A distribution bundle describes the specifications of your distribution, such as the monthly cost and monthly network transfer quota.</p> <p>Use the <code>GetDistributionBundles</code> action to get a list of distribution bundle IDs that you can specify.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_lightsail.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type for the distribution.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the distribution during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    certificate_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSL/TLS certificate that you want to attach to the distribution.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html\">GetCertificates</a> action to get a list of certificate names that you can specify.</p>"""
    viewer_minimum_tls_protocol_version: NotRequired[
        "aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum.ViewerMinimumTlsProtocolVersionEnum"
    ]
    """<p>The minimum TLS protocol version for the SSL/TLS certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDistributionRequest) -> dict:
    out: dict = {}
    out["distributionName"] = value["distribution_name"]
    import aws_sdk_lightsail.types.input_origin

    out["origin"] = aws_sdk_lightsail.types.input_origin.serialize_aws_json_1_1(
        value["origin"]
    )
    import aws_sdk_lightsail.types.cache_behavior

    out["defaultCacheBehavior"] = (
        aws_sdk_lightsail.types.cache_behavior.serialize_aws_json_1_1(
            value["default_cache_behavior"]
        )
    )
    if "cache_behavior_settings" in value:
        import aws_sdk_lightsail.types.cache_settings

        out["cacheBehaviorSettings"] = (
            aws_sdk_lightsail.types.cache_settings.serialize_aws_json_1_1(
                value["cache_behavior_settings"]
            )
        )
    if "cache_behaviors" in value:
        import aws_sdk_lightsail.types.cache_behavior_list

        out["cacheBehaviors"] = (
            aws_sdk_lightsail.types.cache_behavior_list.serialize_aws_json_1_1(
                value["cache_behaviors"]
            )
        )
    out["bundleId"] = value["bundle_id"]
    if "ip_address_type" in value:
        import aws_sdk_lightsail.types.ip_address_type

        out["ipAddressType"] = (
            aws_sdk_lightsail.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "viewer_minimum_tls_protocol_version" in value:
        import aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum

        out["viewerMinimumTlsProtocolVersion"] = (
            aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum.serialize_aws_json_1_1(
                value["viewer_minimum_tls_protocol_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDistributionRequest:
    out: CreateDistributionRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    else:
        raise DeserializationError(
            "CreateDistributionRequest.distribution_name required"
        )
    if "origin" in data:
        import aws_sdk_lightsail.types.input_origin

        out["origin"] = aws_sdk_lightsail.types.input_origin.deserialize_aws_json_1_1(
            data["origin"]
        )
    else:
        raise DeserializationError("CreateDistributionRequest.origin required")
    if "defaultCacheBehavior" in data:
        import aws_sdk_lightsail.types.cache_behavior

        out["default_cache_behavior"] = (
            aws_sdk_lightsail.types.cache_behavior.deserialize_aws_json_1_1(
                data["defaultCacheBehavior"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDistributionRequest.default_cache_behavior required"
        )
    if "cacheBehaviorSettings" in data:
        import aws_sdk_lightsail.types.cache_settings

        out["cache_behavior_settings"] = (
            aws_sdk_lightsail.types.cache_settings.deserialize_aws_json_1_1(
                data["cacheBehaviorSettings"]
            )
        )
    if "cacheBehaviors" in data:
        import aws_sdk_lightsail.types.cache_behavior_list

        out["cache_behaviors"] = (
            aws_sdk_lightsail.types.cache_behavior_list.deserialize_aws_json_1_1(
                data["cacheBehaviors"]
            )
        )
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("CreateDistributionRequest.bundle_id required")
    if "ipAddressType" in data:
        import aws_sdk_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    if "viewerMinimumTlsProtocolVersion" in data:
        import aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum

        out["viewer_minimum_tls_protocol_version"] = (
            aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum.deserialize_aws_json_1_1(
                data["viewerMinimumTlsProtocolVersion"]
            )
        )
    return out
