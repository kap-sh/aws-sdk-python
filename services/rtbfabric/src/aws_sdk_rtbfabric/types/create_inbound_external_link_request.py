"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateInboundExternalLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_attributes
    import aws_sdk_rtbfabric.types.link_log_settings
    import aws_sdk_rtbfabric.types.tags_map


class CreateInboundExternalLinkRequest(TypedDict, closed=True):
    client_token: "str"
    """<p>The unique client token.</p>"""
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    attributes: NotRequired["aws_sdk_rtbfabric.types.link_attributes.LinkAttributes"]
    """<p>Attributes of the link.</p>"""
    log_settings: "aws_sdk_rtbfabric.types.link_log_settings.LinkLogSettings"
    """<p>Settings for the application logs.</p>"""
    tags: NotRequired["aws_sdk_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInboundExternalLinkRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    if "attributes" in value:
        import aws_sdk_rtbfabric.types.link_attributes

        out["attributes"] = aws_sdk_rtbfabric.types.link_attributes.serialize_json(
            value["attributes"]
        )
    import aws_sdk_rtbfabric.types.link_log_settings

    out["logSettings"] = aws_sdk_rtbfabric.types.link_log_settings.serialize_json(
        value["log_settings"]
    )
    if "tags" in value:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateInboundExternalLinkRequest:
    out: CreateInboundExternalLinkRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateInboundExternalLinkRequest.client_token required"
        )
    if "attributes" in data:
        import aws_sdk_rtbfabric.types.link_attributes

        out["attributes"] = aws_sdk_rtbfabric.types.link_attributes.deserialize_json(
            data["attributes"]
        )
    if "logSettings" in data:
        import aws_sdk_rtbfabric.types.link_log_settings

        out["log_settings"] = (
            aws_sdk_rtbfabric.types.link_log_settings.deserialize_json(
                data["logSettings"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInboundExternalLinkRequest.log_settings required"
        )
    if "tags" in data:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    return out
