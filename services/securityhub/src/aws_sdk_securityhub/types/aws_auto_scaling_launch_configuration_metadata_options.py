"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingLaunchConfigurationMetadataOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsAutoScalingLaunchConfigurationMetadataOptions(TypedDict, closed=True):
    http_endpoint: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on your instances. By default, the metadata endpoint is enabled.</p>"""
    http_put_response_hop_limit: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The HTTP <code>PUT</code> response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.</p>"""
    http_tokens: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether token usage is <code>required</code> or <code>optional</code> for metadata requests. By default, token usage is <code>optional</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAutoScalingLaunchConfigurationMetadataOptions) -> dict:
    out: dict = {}
    if "http_endpoint" in value:
        out["HttpEndpoint"] = value["http_endpoint"]
    if "http_put_response_hop_limit" in value:
        out["HttpPutResponseHopLimit"] = value["http_put_response_hop_limit"]
    if "http_tokens" in value:
        out["HttpTokens"] = value["http_tokens"]
    return out


def deserialize_json(data: dict) -> AwsAutoScalingLaunchConfigurationMetadataOptions:
    out: AwsAutoScalingLaunchConfigurationMetadataOptions = {}  # type: ignore[typeddict-item]
    if "HttpEndpoint" in data:
        out["http_endpoint"] = data["HttpEndpoint"]
    if "HttpPutResponseHopLimit" in data:
        out["http_put_response_hop_limit"] = data["HttpPutResponseHopLimit"]
    if "HttpTokens" in data:
        out["http_tokens"] = data["HttpTokens"]
    return out
