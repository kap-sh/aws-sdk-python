"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ChannelHandshakeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.arn
    import capo_partnercentral_channel.types.associated_resource_id
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.channel_handshake_id
    import capo_partnercentral_channel.types.date_time
    import capo_partnercentral_channel.types.handshake_detail
    import capo_partnercentral_channel.types.handshake_status
    import capo_partnercentral_channel.types.handshake_type
    import capo_partnercentral_channel.types.partner_profile_display_name


class ChannelHandshakeSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_channel.types.channel_handshake_id.ChannelHandshakeId"
    ]
    """<p>The unique identifier of the handshake.</p>"""
    arn: NotRequired["capo_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the handshake.</p>"""
    catalog: NotRequired["capo_partnercentral_channel.types.catalog.Catalog"]
    """<p>The catalog identifier associated with the handshake.</p>"""
    handshake_type: NotRequired[
        "capo_partnercentral_channel.types.handshake_type.HandshakeType"
    ]
    """<p>The type of the handshake.</p>"""
    owner_account_id: NotRequired[
        "capo_partnercentral_channel.types.account_id.AccountId"
    ]
    """<p>The AWS account ID of the handshake owner.</p>"""
    sender_account_id: NotRequired[
        "capo_partnercentral_channel.types.account_id.AccountId"
    ]
    """<p>The AWS account ID of the handshake sender.</p>"""
    sender_display_name: NotRequired[
        "capo_partnercentral_channel.types.partner_profile_display_name.PartnerProfileDisplayName"
    ]
    """<p>The display name of the handshake sender.</p>"""
    receiver_account_id: NotRequired[
        "capo_partnercentral_channel.types.account_id.AccountId"
    ]
    """<p>The AWS account ID of the handshake receiver.</p>"""
    associated_resource_id: NotRequired[
        "capo_partnercentral_channel.types.associated_resource_id.AssociatedResourceId"
    ]
    """<p>The identifier of the resource associated with the handshake.</p>"""
    detail: NotRequired[
        "capo_partnercentral_channel.types.handshake_detail.HandshakeDetail"
    ]
    """<p>Detailed information about the handshake.</p>"""
    created_at: NotRequired["capo_partnercentral_channel.types.date_time.DateTime"]
    """<p>The timestamp when the handshake was created.</p>"""
    updated_at: NotRequired["capo_partnercentral_channel.types.date_time.DateTime"]
    """<p>The timestamp when the handshake was last updated.</p>"""
    status: NotRequired[
        "capo_partnercentral_channel.types.handshake_status.HandshakeStatus"
    ]
    """<p>The current status of the handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChannelHandshakeSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "handshake_type" in value:
        import capo_partnercentral_channel.types.handshake_type

        out["handshakeType"] = (
            capo_partnercentral_channel.types.handshake_type.serialize_aws_json_1_0(
                value["handshake_type"]
            )
        )
    if "owner_account_id" in value:
        out["ownerAccountId"] = value["owner_account_id"]
    if "sender_account_id" in value:
        out["senderAccountId"] = value["sender_account_id"]
    if "sender_display_name" in value:
        out["senderDisplayName"] = value["sender_display_name"]
    if "receiver_account_id" in value:
        out["receiverAccountId"] = value["receiver_account_id"]
    if "associated_resource_id" in value:
        out["associatedResourceId"] = value["associated_resource_id"]
    if "detail" in value:
        import capo_partnercentral_channel.types.handshake_detail

        out["detail"] = (
            capo_partnercentral_channel.types.handshake_detail.serialize_aws_json_1_0(
                value["detail"]
            )
        )
    if "created_at" in value:
        import capo_partnercentral_channel.types.date_time

        out["createdAt"] = (
            capo_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_partnercentral_channel.types.date_time

        out["updatedAt"] = (
            capo_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "status" in value:
        import capo_partnercentral_channel.types.handshake_status

        out["status"] = (
            capo_partnercentral_channel.types.handshake_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ChannelHandshakeSummary:
    out: ChannelHandshakeSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    if "handshakeType" in data:
        import capo_partnercentral_channel.types.handshake_type

        out["handshake_type"] = (
            capo_partnercentral_channel.types.handshake_type.deserialize_aws_json_1_0(
                data["handshakeType"]
            )
        )
    if "ownerAccountId" in data:
        out["owner_account_id"] = data["ownerAccountId"]
    if "senderAccountId" in data:
        out["sender_account_id"] = data["senderAccountId"]
    if "senderDisplayName" in data:
        out["sender_display_name"] = data["senderDisplayName"]
    if "receiverAccountId" in data:
        out["receiver_account_id"] = data["receiverAccountId"]
    if "associatedResourceId" in data:
        out["associated_resource_id"] = data["associatedResourceId"]
    if "detail" in data:
        import capo_partnercentral_channel.types.handshake_detail

        out["detail"] = (
            capo_partnercentral_channel.types.handshake_detail.deserialize_aws_json_1_0(
                data["detail"]
            )
        )
    if "createdAt" in data:
        import capo_partnercentral_channel.types.date_time

        out["created_at"] = (
            capo_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_partnercentral_channel.types.date_time

        out["updated_at"] = (
            capo_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if "status" in data:
        import capo_partnercentral_channel.types.handshake_status

        out["status"] = (
            capo_partnercentral_channel.types.handshake_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
