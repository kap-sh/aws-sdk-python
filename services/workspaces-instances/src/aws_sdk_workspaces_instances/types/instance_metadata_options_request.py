"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.http_endpoint_enum
    import aws_sdk_workspaces_instances.types.http_protocol_ipv6_enum
    import aws_sdk_workspaces_instances.types.http_put_response_hop_limit
    import aws_sdk_workspaces_instances.types.http_tokens_enum
    import aws_sdk_workspaces_instances.types.instance_metadata_tags_enum


class InstanceMetadataOptionsRequest(TypedDict):
    http_endpoint: NotRequired[
        "aws_sdk_workspaces_instances.types.http_endpoint_enum.HttpEndpointEnum"
    ]
    """<p>Enables or disables HTTP endpoint for instance metadata.</p>"""
    http_protocol_ipv6: NotRequired[
        "aws_sdk_workspaces_instances.types.http_protocol_ipv6_enum.HttpProtocolIpv6Enum"
    ]
    """<p>Configures IPv6 support for instance metadata HTTP protocol.</p>"""
    http_put_response_hop_limit: NotRequired[
        "aws_sdk_workspaces_instances.types.http_put_response_hop_limit.HttpPutResponseHopLimit"
    ]
    """<p>Sets maximum number of network hops for metadata PUT responses.</p>"""
    http_tokens: NotRequired[
        "aws_sdk_workspaces_instances.types.http_tokens_enum.HttpTokensEnum"
    ]
    """<p>Configures token requirement for instance metadata retrieval.</p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_workspaces_instances.types.instance_metadata_tags_enum.InstanceMetadataTagsEnum"
    ]
    """<p>Enables or disables instance metadata tags retrieval.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceMetadataOptionsRequest) -> dict:
    out: dict = {}
    if "http_endpoint" in value:
        import aws_sdk_workspaces_instances.types.http_endpoint_enum

        out["HttpEndpoint"] = (
            aws_sdk_workspaces_instances.types.http_endpoint_enum.serialize_aws_json_1_0(
                value["http_endpoint"]
            )
        )
    if "http_protocol_ipv6" in value:
        import aws_sdk_workspaces_instances.types.http_protocol_ipv6_enum

        out["HttpProtocolIpv6"] = (
            aws_sdk_workspaces_instances.types.http_protocol_ipv6_enum.serialize_aws_json_1_0(
                value["http_protocol_ipv6"]
            )
        )
    if "http_put_response_hop_limit" in value:
        out["HttpPutResponseHopLimit"] = value["http_put_response_hop_limit"]
    if "http_tokens" in value:
        import aws_sdk_workspaces_instances.types.http_tokens_enum

        out["HttpTokens"] = (
            aws_sdk_workspaces_instances.types.http_tokens_enum.serialize_aws_json_1_0(
                value["http_tokens"]
            )
        )
    if "instance_metadata_tags" in value:
        import aws_sdk_workspaces_instances.types.instance_metadata_tags_enum

        out["InstanceMetadataTags"] = (
            aws_sdk_workspaces_instances.types.instance_metadata_tags_enum.serialize_aws_json_1_0(
                value["instance_metadata_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceMetadataOptionsRequest:
    out: InstanceMetadataOptionsRequest = {}  # type: ignore[typeddict-item]
    if "HttpEndpoint" in data:
        import aws_sdk_workspaces_instances.types.http_endpoint_enum

        out["http_endpoint"] = (
            aws_sdk_workspaces_instances.types.http_endpoint_enum.deserialize_aws_json_1_0(
                data["HttpEndpoint"]
            )
        )
    if "HttpProtocolIpv6" in data:
        import aws_sdk_workspaces_instances.types.http_protocol_ipv6_enum

        out["http_protocol_ipv6"] = (
            aws_sdk_workspaces_instances.types.http_protocol_ipv6_enum.deserialize_aws_json_1_0(
                data["HttpProtocolIpv6"]
            )
        )
    if "HttpPutResponseHopLimit" in data:
        out["http_put_response_hop_limit"] = data["HttpPutResponseHopLimit"]
    if "HttpTokens" in data:
        import aws_sdk_workspaces_instances.types.http_tokens_enum

        out["http_tokens"] = (
            aws_sdk_workspaces_instances.types.http_tokens_enum.deserialize_aws_json_1_0(
                data["HttpTokens"]
            )
        )
    if "InstanceMetadataTags" in data:
        import aws_sdk_workspaces_instances.types.instance_metadata_tags_enum

        out["instance_metadata_tags"] = (
            aws_sdk_workspaces_instances.types.instance_metadata_tags_enum.deserialize_aws_json_1_0(
                data["InstanceMetadataTags"]
            )
        )
    return out
