"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateChannelHandshakeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.associated_resource_identifier
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.channel_handshake_payload
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.handshake_type
    import capo_partnercentral_channel.types.tag_list


class CreateChannelHandshakeRequest(TypedDict, closed=True):
    handshake_type: "capo_partnercentral_channel.types.handshake_type.HandshakeType"
    """<p>The type of handshake to create (e.g., start service period, revoke service period).</p>"""
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the handshake request.</p>"""
    associated_resource_identifier: "capo_partnercentral_channel.types.associated_resource_identifier.AssociatedResourceIdentifier"
    """<p>The identifier of the resource associated with this handshake.</p>"""
    payload: NotRequired[
        "capo_partnercentral_channel.types.channel_handshake_payload.ChannelHandshakePayload"
    ]
    """<p>The payload containing specific details for the handshake type.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    tags: NotRequired["capo_partnercentral_channel.types.tag_list.TagList"]
    """<p>Key-value pairs to associate with the channel handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateChannelHandshakeRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_channel.types.handshake_type

    out["handshakeType"] = (
        capo_partnercentral_channel.types.handshake_type.serialize_aws_json_1_0(
            value["handshake_type"]
        )
    )
    out["catalog"] = value["catalog"]
    out["associatedResourceIdentifier"] = value["associated_resource_identifier"]
    if "payload" in value:
        import capo_partnercentral_channel.types.channel_handshake_payload

        out["payload"] = (
            capo_partnercentral_channel.types.channel_handshake_payload.serialize_aws_json_1_0(
                value["payload"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = capo_partnercentral_channel.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateChannelHandshakeRequest:
    out: CreateChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
    if "handshakeType" in data:
        import capo_partnercentral_channel.types.handshake_type

        out["handshake_type"] = (
            capo_partnercentral_channel.types.handshake_type.deserialize_aws_json_1_0(
                data["handshakeType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateChannelHandshakeRequest.handshake_type required"
        )
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("CreateChannelHandshakeRequest.catalog required")
    if "associatedResourceIdentifier" in data:
        out["associated_resource_identifier"] = data["associatedResourceIdentifier"]
    else:
        raise DeserializationError(
            "CreateChannelHandshakeRequest.associated_resource_identifier required"
        )
    if "payload" in data:
        import capo_partnercentral_channel.types.channel_handshake_payload

        out["payload"] = (
            capo_partnercentral_channel.types.channel_handshake_payload.deserialize_aws_json_1_0(
                data["payload"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = (
            capo_partnercentral_channel.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
