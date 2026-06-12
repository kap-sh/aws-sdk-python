"""Generated from Smithy shape ``com.amazonaws.lightsail#LightsailDistribution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.cache_behavior
    import aws_sdk_lightsail.types.cache_behavior_list
    import aws_sdk_lightsail.types.cache_settings
    import aws_sdk_lightsail.types.ip_address_type
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.origin
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.string_list
    import aws_sdk_lightsail.types.tag_list


class LightsailDistribution(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the distribution.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the distribution.</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about your Lightsail distribution. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the distribution was created.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>An object that describes the location of the distribution, such as the Amazon Web Services Region and Availability Zone.</p> <note> <p>Lightsail distributions are global resources that can reference an origin in any Amazon Web Services Region, and distribute its content globally. However, all distributions are located in the <code>us-east-1</code> Region.</p> </note>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type (<code>Distribution</code>).</p>"""
    alternative_domain_names: NotRequired[
        "aws_sdk_lightsail.types.string_list.StringList"
    ]
    """<p>The alternate domain names of the distribution.</p>"""
    status: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The status of the distribution.</p>"""
    is_enabled: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the distribution is enabled.</p>"""
    domain_name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The domain name of the distribution.</p>"""
    bundle_id: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The ID of the bundle currently applied to the distribution.</p>"""
    certificate_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSL/TLS certificate attached to the distribution, if any.</p>"""
    origin: NotRequired["aws_sdk_lightsail.types.origin.Origin"]
    """<p>An object that describes the origin resource of the distribution, such as a Lightsail instance, bucket, or load balancer.</p> <p>The distribution pulls, caches, and serves content from the origin.</p>"""
    origin_public_dns: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The public DNS of the origin.</p>"""
    default_cache_behavior: NotRequired[
        "aws_sdk_lightsail.types.cache_behavior.CacheBehavior"
    ]
    """<p>An object that describes the default cache behavior of the distribution.</p>"""
    cache_behavior_settings: NotRequired[
        "aws_sdk_lightsail.types.cache_settings.CacheSettings"
    ]
    """<p>An object that describes the cache behavior settings of the distribution.</p>"""
    cache_behaviors: NotRequired[
        "aws_sdk_lightsail.types.cache_behavior_list.CacheBehaviorList"
    ]
    """<p>An array of objects that describe the per-path cache behavior of the distribution.</p>"""
    able_to_update_bundle: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the bundle that is currently applied to your distribution, specified using the <code>distributionName</code> parameter, can be changed to another bundle.</p> <p>Use the <code>UpdateDistributionBundle</code> action to change your distribution's bundle.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_lightsail.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type of the distribution.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, and <code>dualstack</code> for IPv4 and IPv6.</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""
    viewer_minimum_tls_protocol_version: NotRequired[
        "aws_sdk_lightsail.types.string.string"
    ]
    """<p>The minimum TLS protocol version that the distribution can use to communicate with viewers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LightsailDistribution) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "alternative_domain_names" in value:
        import aws_sdk_lightsail.types.string_list

        out["alternativeDomainNames"] = (
            aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
                value["alternative_domain_names"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "is_enabled" in value:
        out["isEnabled"] = value["is_enabled"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "origin" in value:
        import aws_sdk_lightsail.types.origin

        out["origin"] = aws_sdk_lightsail.types.origin.serialize_aws_json_1_1(
            value["origin"]
        )
    if "origin_public_dns" in value:
        out["originPublicDNS"] = value["origin_public_dns"]
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
    if "able_to_update_bundle" in value:
        out["ableToUpdateBundle"] = value["able_to_update_bundle"]
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
    if "viewer_minimum_tls_protocol_version" in value:
        out["viewerMinimumTlsProtocolVersion"] = value[
            "viewer_minimum_tls_protocol_version"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> LightsailDistribution:
    out: LightsailDistribution = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "supportCode" in data:
        out["support_code"] = data["supportCode"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "alternativeDomainNames" in data:
        import aws_sdk_lightsail.types.string_list

        out["alternative_domain_names"] = (
            aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["alternativeDomainNames"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "isEnabled" in data:
        out["is_enabled"] = data["isEnabled"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    if "origin" in data:
        import aws_sdk_lightsail.types.origin

        out["origin"] = aws_sdk_lightsail.types.origin.deserialize_aws_json_1_1(
            data["origin"]
        )
    if "originPublicDNS" in data:
        out["origin_public_dns"] = data["originPublicDNS"]
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
    if "ableToUpdateBundle" in data:
        out["able_to_update_bundle"] = data["ableToUpdateBundle"]
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
    if "viewerMinimumTlsProtocolVersion" in data:
        out["viewer_minimum_tls_protocol_version"] = data[
            "viewerMinimumTlsProtocolVersion"
        ]
    return out
