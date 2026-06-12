"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateInstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.http_endpoint
    import aws_sdk_lightsail.types.http_protocol_ipv6
    import aws_sdk_lightsail.types.http_tokens
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.resource_name


class UpdateInstanceMetadataOptionsRequest(TypedDict):
    instance_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance for which to update metadata parameters.</p>"""
    http_tokens: NotRequired["aws_sdk_lightsail.types.http_tokens.HttpTokens"]
    """<p>The state of token usage for your instance metadata requests. If the parameter is not specified in the request, the default state is <code>optional</code>.</p> <p>If the state is <code>optional</code>, you can choose whether to retrieve instance metadata with a signed token header on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials by using a valid signed token, the version 2.0 role credentials are returned.</p> <p>If the state is <code>required</code>, you must send a signed token header with all instance metadata retrieval requests. In this state, retrieving the IAM role credential always returns the version 2.0 credentials. The version 1.0 credentials are not available.</p>"""
    http_endpoint: NotRequired["aws_sdk_lightsail.types.http_endpoint.HttpEndpoint"]
    """<p>Enables or disables the HTTP metadata endpoint on your instances. If this parameter is not specified, the existing state is maintained.</p> <p>If you specify a value of <code>disabled</code>, you cannot access your instance metadata.</p>"""
    http_put_response_hop_limit: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. A larger number means that the instance metadata requests can travel farther. If no parameter is specified, the existing state is maintained.</p>"""
    http_protocol_ipv6: NotRequired[
        "aws_sdk_lightsail.types.http_protocol_ipv6.HttpProtocolIpv6"
    ]
    """<p>Enables or disables the IPv6 endpoint for the instance metadata service. This setting applies only when the HTTP metadata endpoint is enabled.</p> <note> <p>This parameter is available only for instances in the Europe (Stockholm) Amazon Web Services Region (<code>eu-north-1</code>).</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInstanceMetadataOptionsRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    if "http_tokens" in value:
        import aws_sdk_lightsail.types.http_tokens

        out["httpTokens"] = aws_sdk_lightsail.types.http_tokens.serialize_aws_json_1_1(
            value["http_tokens"]
        )
    if "http_endpoint" in value:
        import aws_sdk_lightsail.types.http_endpoint

        out["httpEndpoint"] = (
            aws_sdk_lightsail.types.http_endpoint.serialize_aws_json_1_1(
                value["http_endpoint"]
            )
        )
    if "http_put_response_hop_limit" in value:
        out["httpPutResponseHopLimit"] = value["http_put_response_hop_limit"]
    if "http_protocol_ipv6" in value:
        import aws_sdk_lightsail.types.http_protocol_ipv6

        out["httpProtocolIpv6"] = (
            aws_sdk_lightsail.types.http_protocol_ipv6.serialize_aws_json_1_1(
                value["http_protocol_ipv6"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInstanceMetadataOptionsRequest:
    out: UpdateInstanceMetadataOptionsRequest = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError(
            "UpdateInstanceMetadataOptionsRequest.instance_name required"
        )
    if "httpTokens" in data:
        import aws_sdk_lightsail.types.http_tokens

        out["http_tokens"] = (
            aws_sdk_lightsail.types.http_tokens.deserialize_aws_json_1_1(
                data["httpTokens"]
            )
        )
    if "httpEndpoint" in data:
        import aws_sdk_lightsail.types.http_endpoint

        out["http_endpoint"] = (
            aws_sdk_lightsail.types.http_endpoint.deserialize_aws_json_1_1(
                data["httpEndpoint"]
            )
        )
    if "httpPutResponseHopLimit" in data:
        out["http_put_response_hop_limit"] = data["httpPutResponseHopLimit"]
    if "httpProtocolIpv6" in data:
        import aws_sdk_lightsail.types.http_protocol_ipv6

        out["http_protocol_ipv6"] = (
            aws_sdk_lightsail.types.http_protocol_ipv6.deserialize_aws_json_1_1(
                data["httpProtocolIpv6"]
            )
        )
    return out
