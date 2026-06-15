"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.cache_behavior
    import aws_sdk_lightsail.types.cache_behavior_list
    import aws_sdk_lightsail.types.cache_settings
    import aws_sdk_lightsail.types.input_origin
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum


class UpdateDistributionRequest(TypedDict):
    distribution_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the distribution to update.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""
    origin: NotRequired["aws_sdk_lightsail.types.input_origin.InputOrigin"]
    """<p>An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.</p> <p>The distribution pulls, caches, and serves content from the origin.</p>"""
    default_cache_behavior: NotRequired[
        "aws_sdk_lightsail.types.cache_behavior.CacheBehavior"
    ]
    """<p>An object that describes the default cache behavior for the distribution.</p>"""
    cache_behavior_settings: NotRequired[
        "aws_sdk_lightsail.types.cache_settings.CacheSettings"
    ]
    """<p>An object that describes the cache behavior settings for the distribution.</p> <note> <p>The <code>cacheBehaviorSettings</code> specified in your <code>UpdateDistributionRequest</code> will replace your distribution's existing settings.</p> </note>"""
    cache_behaviors: NotRequired[
        "aws_sdk_lightsail.types.cache_behavior_list.CacheBehaviorList"
    ]
    """<p>An array of objects that describe the per-path cache behavior for the distribution.</p>"""
    is_enabled: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>Indicates whether to enable the distribution.</p>"""
    viewer_minimum_tls_protocol_version: NotRequired[
        "aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum.ViewerMinimumTlsProtocolVersionEnum"
    ]
    """<p>Use this parameter to update the minimum TLS protocol version for the SSL/TLS certificate that's attached to the distribution.</p>"""
    certificate_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    r"""<p>The name of the SSL/TLS certificate that you want to attach to the distribution.</p> <p>Only certificates with a status of <code>ISSUED</code> can be attached to a distribution.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html\">GetCertificates</a> action to get a list of certificate names that you can specify.</p>"""
    use_default_certificate: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the default SSL/TLS certificate is attached to the distribution. The default value is <code>true</code>. When <code>true</code>, the distribution uses the default domain name such as <code>d111111abcdef8.cloudfront.net</code>.</p> <p> Set this value to <code>false</code> to attach a new certificate to the distribution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDistributionRequest) -> dict:
    out: dict = {}
    out["distributionName"] = value["distribution_name"]
    if "origin" in value:
        import aws_sdk_lightsail.types.input_origin

        out["origin"] = aws_sdk_lightsail.types.input_origin.serialize_aws_json_1_1(
            value["origin"]
        )
    if "default_cache_behavior" in value:
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
    if "is_enabled" in value:
        out["isEnabled"] = value["is_enabled"]
    if "viewer_minimum_tls_protocol_version" in value:
        import aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum

        out["viewerMinimumTlsProtocolVersion"] = (
            aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum.serialize_aws_json_1_1(
                value["viewer_minimum_tls_protocol_version"]
            )
        )
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "use_default_certificate" in value:
        out["useDefaultCertificate"] = value["use_default_certificate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDistributionRequest:
    out: UpdateDistributionRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    else:
        raise DeserializationError(
            "UpdateDistributionRequest.distribution_name required"
        )
    if "origin" in data:
        import aws_sdk_lightsail.types.input_origin

        out["origin"] = aws_sdk_lightsail.types.input_origin.deserialize_aws_json_1_1(
            data["origin"]
        )
    if "defaultCacheBehavior" in data:
        import aws_sdk_lightsail.types.cache_behavior

        out["default_cache_behavior"] = (
            aws_sdk_lightsail.types.cache_behavior.deserialize_aws_json_1_1(
                data["defaultCacheBehavior"]
            )
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
    if "isEnabled" in data:
        out["is_enabled"] = data["isEnabled"]
    if "viewerMinimumTlsProtocolVersion" in data:
        import aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum

        out["viewer_minimum_tls_protocol_version"] = (
            aws_sdk_lightsail.types.viewer_minimum_tls_protocol_version_enum.deserialize_aws_json_1_1(
                data["viewerMinimumTlsProtocolVersion"]
            )
        )
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    if "useDefaultCertificate" in data:
        out["use_default_certificate"] = data["useDefaultCertificate"]
    return out
