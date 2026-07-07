"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceMetadataOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.http_endpoint
    import aws_sdk_lightsail.types.http_protocol_ipv6
    import aws_sdk_lightsail.types.http_tokens
    import aws_sdk_lightsail.types.instance_metadata_state
    import aws_sdk_lightsail.types.integer


class InstanceMetadataOptions(TypedDict, closed=True):
    state: NotRequired[
        "aws_sdk_lightsail.types.instance_metadata_state.InstanceMetadataState"
    ]
    """<p>The state of the metadata option changes.</p> <p>The following states are possible:</p> <ul> <li> <p> <code>pending</code> - The metadata options are being updated. The instance is not yet ready to process metadata traffic with the new selection.</p> </li> <li> <p> <code>applied</code> - The metadata options have been successfully applied to the instance.</p> </li> </ul>"""
    http_tokens: NotRequired["aws_sdk_lightsail.types.http_tokens.HttpTokens"]
    r"""<p>The state of token usage for your instance metadata requests.</p> <p>If the state is <code>optional</code>, you can choose whether to retrieve instance metadata with a signed token header on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials by using a valid signed token, the version 2.0 role credentials are returned.</p> <p>If the state is <code>required</code>, you must send a signed token header with all instance metadata retrieval requests. In this state, retrieving the IAM role credential always returns the version 2.0 credentials. The version 1.0 credentials are not available.</p> <important> <p>Not all instance blueprints in Lightsail support version 2.0 credentials. Use the <code>MetadataNoToken</code> instance metric to track the number of calls to the instance metadata service that are using version 1.0 credentials. For more information, see <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-health-metrics\">Viewing instance metrics in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p> </important>"""
    http_endpoint: NotRequired["aws_sdk_lightsail.types.http_endpoint.HttpEndpoint"]
    """<p>Indicates whether the HTTP metadata endpoint on your instances is enabled or disabled.</p> <p>If the value is <code>disabled</code>, you cannot access your instance metadata.</p>"""
    http_put_response_hop_limit: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. A larger number means that the instance metadata requests can travel farther.</p>"""
    http_protocol_ipv6: NotRequired[
        "aws_sdk_lightsail.types.http_protocol_ipv6.HttpProtocolIpv6"
    ]
    """<p>Indicates whether the IPv6 endpoint for the instance metadata service is enabled or disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceMetadataOptions) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_lightsail.types.instance_metadata_state

        out["state"] = (
            aws_sdk_lightsail.types.instance_metadata_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> InstanceMetadataOptions:
    out: InstanceMetadataOptions = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_lightsail.types.instance_metadata_state

        out["state"] = (
            aws_sdk_lightsail.types.instance_metadata_state.deserialize_aws_json_1_1(
                data["state"]
            )
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
