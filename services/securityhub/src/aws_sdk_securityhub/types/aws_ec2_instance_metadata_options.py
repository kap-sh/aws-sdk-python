"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2InstanceMetadataOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2InstanceMetadataOptions(TypedDict):
    http_endpoint: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on the instance. </p>"""
    http_protocol_ipv6: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Enables or disables the IPv6 endpoint for the instance metadata service. </p>"""
    http_put_response_hop_limit: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel. </p>"""
    http_tokens: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The state of token usage for your instance metadata requests. </p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies whether to allow access to instance tags from the instance metadata. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2InstanceMetadataOptions) -> dict:
    out: dict = {}
    if "http_endpoint" in value:
        out["HttpEndpoint"] = value["http_endpoint"]
    if "http_protocol_ipv6" in value:
        out["HttpProtocolIpv6"] = value["http_protocol_ipv6"]
    if "http_put_response_hop_limit" in value:
        out["HttpPutResponseHopLimit"] = value["http_put_response_hop_limit"]
    if "http_tokens" in value:
        out["HttpTokens"] = value["http_tokens"]
    if "instance_metadata_tags" in value:
        out["InstanceMetadataTags"] = value["instance_metadata_tags"]
    return out


def deserialize_json(data: dict) -> AwsEc2InstanceMetadataOptions:
    out: AwsEc2InstanceMetadataOptions = {}  # type: ignore[typeddict-item]
    if "HttpEndpoint" in data:
        out["http_endpoint"] = data["HttpEndpoint"]
    if "HttpProtocolIpv6" in data:
        out["http_protocol_ipv6"] = data["HttpProtocolIpv6"]
    if "HttpPutResponseHopLimit" in data:
        out["http_put_response_hop_limit"] = data["HttpPutResponseHopLimit"]
    if "HttpTokens" in data:
        out["http_tokens"] = data["HttpTokens"]
    if "InstanceMetadataTags" in data:
        out["instance_metadata_tags"] = data["InstanceMetadataTags"]
    return out
