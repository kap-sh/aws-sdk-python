"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateLinkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_attributes
    import aws_sdk_rtbfabric.types.link_log_settings
    import aws_sdk_rtbfabric.types.link_timeout_in_millis
    import aws_sdk_rtbfabric.types.tags_map


class CreateLinkRequest(TypedDict):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    peer_gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the peer gateway.</p>"""
    attributes: NotRequired["aws_sdk_rtbfabric.types.link_attributes.LinkAttributes"]
    """<p>Attributes of the link.</p>"""
    http_responder_allowed: NotRequired["bool"]
    """<p>Boolean to specify if an HTTP responder is allowed.</p>"""
    tags: NotRequired["aws_sdk_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""
    log_settings: "aws_sdk_rtbfabric.types.link_log_settings.LinkLogSettings"
    """<p>Settings for the application logs.</p>"""
    timeout_in_millis: NotRequired[
        "aws_sdk_rtbfabric.types.link_timeout_in_millis.LinkTimeoutInMillis"
    ]
    """<p>The timeout value in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkRequest) -> dict:
    out: dict = {}
    out["peerGatewayId"] = value["peer_gateway_id"]
    if "attributes" in value:
        import aws_sdk_rtbfabric.types.link_attributes

        out["attributes"] = aws_sdk_rtbfabric.types.link_attributes.serialize_json(
            value["attributes"]
        )
    if "http_responder_allowed" in value:
        out["httpResponderAllowed"] = value["http_responder_allowed"]
    if "tags" in value:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.serialize_json(value["tags"])
    import aws_sdk_rtbfabric.types.link_log_settings

    out["logSettings"] = aws_sdk_rtbfabric.types.link_log_settings.serialize_json(
        value["log_settings"]
    )
    if "timeout_in_millis" in value:
        out["timeoutInMillis"] = value["timeout_in_millis"]
    return out


def deserialize_json(data: dict) -> CreateLinkRequest:
    out: CreateLinkRequest = {}  # type: ignore[typeddict-item]
    if "peerGatewayId" in data:
        out["peer_gateway_id"] = data["peerGatewayId"]
    else:
        raise DeserializationError("CreateLinkRequest.peer_gateway_id required")
    if "attributes" in data:
        import aws_sdk_rtbfabric.types.link_attributes

        out["attributes"] = aws_sdk_rtbfabric.types.link_attributes.deserialize_json(
            data["attributes"]
        )
    if "httpResponderAllowed" in data:
        out["http_responder_allowed"] = data["httpResponderAllowed"]
    if "tags" in data:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if "logSettings" in data:
        import aws_sdk_rtbfabric.types.link_log_settings

        out["log_settings"] = (
            aws_sdk_rtbfabric.types.link_log_settings.deserialize_json(
                data["logSettings"]
            )
        )
    else:
        raise DeserializationError("CreateLinkRequest.log_settings required")
    if "timeoutInMillis" in data:
        out["timeout_in_millis"] = data["timeoutInMillis"]
    return out
