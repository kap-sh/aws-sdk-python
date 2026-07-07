"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CancelConnectionInvitationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.connection_id
    import aws_sdk_partnercentral_account.types.connection_invitation_arn
    import aws_sdk_partnercentral_account.types.connection_invitation_id
    import aws_sdk_partnercentral_account.types.connection_type
    import aws_sdk_partnercentral_account.types.date_time
    import aws_sdk_partnercentral_account.types.email
    import aws_sdk_partnercentral_account.types.invitation_status
    import aws_sdk_partnercentral_account.types.participant_identifier
    import aws_sdk_partnercentral_account.types.participant_type
    import aws_sdk_partnercentral_account.types.sensitive_unicode_string
    import aws_sdk_partnercentral_account.types.unicode_string_including_new_line


class CancelConnectionInvitationResponse(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection invitation was canceled.</p>"""
    id: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId"
    """<p>The unique identifier of the canceled connection invitation.</p>"""
    arn: "aws_sdk_partnercentral_account.types.connection_invitation_arn.ConnectionInvitationArn"
    """<p>The Amazon Resource Name (ARN) of the canceled connection invitation.</p>"""
    connection_id: NotRequired[
        "aws_sdk_partnercentral_account.types.connection_id.ConnectionId"
    ]
    """<p>The identifier of the connection associated with the canceled invitation.</p>"""
    connection_type: (
        "aws_sdk_partnercentral_account.types.connection_type.ConnectionType"
    )
    """<p>The type of connection that was being invited for.</p>"""
    created_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection invitation was originally created.</p>"""
    updated_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection invitation was last updated (canceled).</p>"""
    expires_at: NotRequired["aws_sdk_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the connection invitation would have expired if not canceled.</p>"""
    other_participant_identifier: "aws_sdk_partnercentral_account.types.participant_identifier.ParticipantIdentifier"
    """<p>The identifier of the other participant who was invited to connect.</p>"""
    participant_type: (
        "aws_sdk_partnercentral_account.types.participant_type.ParticipantType"
    )
    """<p>The type of participant (inviter or invitee) in the connection invitation.</p>"""
    status: "aws_sdk_partnercentral_account.types.invitation_status.InvitationStatus"
    """<p>The current status of the connection invitation (canceled).</p>"""
    invitation_message: "aws_sdk_partnercentral_account.types.unicode_string_including_new_line.UnicodeStringIncludingNewLine"
    """<p>The message that was included with the original connection invitation.</p>"""
    inviter_email: "aws_sdk_partnercentral_account.types.email.Email"
    """<p>The email address of the person who sent the connection invitation.</p>"""
    inviter_name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The name of the person who sent the connection invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelConnectionInvitationResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    if "connection_id" in value:
        out["ConnectionId"] = value["connection_id"]
    import aws_sdk_partnercentral_account.types.connection_type

    out["ConnectionType"] = (
        aws_sdk_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
            value["connection_type"]
        )
    )
    import aws_sdk_partnercentral_account.types.date_time

    out["CreatedAt"] = (
        aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import aws_sdk_partnercentral_account.types.date_time

    out["UpdatedAt"] = (
        aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    if "expires_at" in value:
        import aws_sdk_partnercentral_account.types.date_time

        out["ExpiresAt"] = (
            aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    out["OtherParticipantIdentifier"] = value["other_participant_identifier"]
    import aws_sdk_partnercentral_account.types.participant_type

    out["ParticipantType"] = (
        aws_sdk_partnercentral_account.types.participant_type.serialize_aws_json_1_0(
            value["participant_type"]
        )
    )
    import aws_sdk_partnercentral_account.types.invitation_status

    out["Status"] = (
        aws_sdk_partnercentral_account.types.invitation_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    out["InvitationMessage"] = value["invitation_message"]
    out["InviterEmail"] = value["inviter_email"]
    out["InviterName"] = value["inviter_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelConnectionInvitationResponse:
    out: CancelConnectionInvitationResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.catalog required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CancelConnectionInvitationResponse.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CancelConnectionInvitationResponse.arn required")
    if "ConnectionId" in data:
        out["connection_id"] = data["ConnectionId"]
    if "ConnectionType" in data:
        import aws_sdk_partnercentral_account.types.connection_type

        out["connection_type"] = (
            aws_sdk_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                data["ConnectionType"]
            )
        )
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.connection_type required"
        )
    if "CreatedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["created_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.created_at required"
        )
    if "UpdatedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["updated_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.updated_at required"
        )
    if "ExpiresAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["expires_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["ExpiresAt"]
            )
        )
    if "OtherParticipantIdentifier" in data:
        out["other_participant_identifier"] = data["OtherParticipantIdentifier"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.other_participant_identifier required"
        )
    if "ParticipantType" in data:
        import aws_sdk_partnercentral_account.types.participant_type

        out["participant_type"] = (
            aws_sdk_partnercentral_account.types.participant_type.deserialize_aws_json_1_0(
                data["ParticipantType"]
            )
        )
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.participant_type required"
        )
    if "Status" in data:
        import aws_sdk_partnercentral_account.types.invitation_status

        out["status"] = (
            aws_sdk_partnercentral_account.types.invitation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CancelConnectionInvitationResponse.status required")
    if "InvitationMessage" in data:
        out["invitation_message"] = data["InvitationMessage"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.invitation_message required"
        )
    if "InviterEmail" in data:
        out["inviter_email"] = data["InviterEmail"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.inviter_email required"
        )
    if "InviterName" in data:
        out["inviter_name"] = data["InviterName"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.inviter_name required"
        )
    return out
