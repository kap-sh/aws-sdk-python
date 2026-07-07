"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionInvitationSummary``."""

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
    import aws_sdk_partnercentral_account.types.invitation_status
    import aws_sdk_partnercentral_account.types.participant_identifier
    import aws_sdk_partnercentral_account.types.participant_type


class ConnectionInvitationSummary(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection invitation exists.</p>"""
    id: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId"
    """<p>The unique identifier of the connection invitation.</p>"""
    arn: "aws_sdk_partnercentral_account.types.connection_invitation_arn.ConnectionInvitationArn"
    """<p>The Amazon Resource Name (ARN) of the connection invitation.</p>"""
    connection_id: NotRequired[
        "aws_sdk_partnercentral_account.types.connection_id.ConnectionId"
    ]
    """<p>The identifier of the connection associated with this invitation.</p>"""
    connection_type: (
        "aws_sdk_partnercentral_account.types.connection_type.ConnectionType"
    )
    """<p>The type of connection being requested in the invitation.</p>"""
    created_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection invitation was created.</p>"""
    updated_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection invitation was last updated.</p>"""
    expires_at: NotRequired["aws_sdk_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the connection invitation will expire.</p>"""
    other_participant_identifier: "aws_sdk_partnercentral_account.types.participant_identifier.ParticipantIdentifier"
    """<p>The identifier of the other participant in the connection invitation.</p>"""
    participant_type: (
        "aws_sdk_partnercentral_account.types.participant_type.ParticipantType"
    )
    """<p>The type of participant (inviter or invitee) in the connection invitation.</p>"""
    status: "aws_sdk_partnercentral_account.types.invitation_status.InvitationStatus"
    """<p>The current status of the connection invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionInvitationSummary) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionInvitationSummary:
    out: ConnectionInvitationSummary = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ConnectionInvitationSummary.catalog required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("ConnectionInvitationSummary.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ConnectionInvitationSummary.arn required")
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
            "ConnectionInvitationSummary.connection_type required"
        )
    if "CreatedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["created_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("ConnectionInvitationSummary.created_at required")
    if "UpdatedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["updated_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError("ConnectionInvitationSummary.updated_at required")
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
            "ConnectionInvitationSummary.other_participant_identifier required"
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
            "ConnectionInvitationSummary.participant_type required"
        )
    if "Status" in data:
        import aws_sdk_partnercentral_account.types.invitation_status

        out["status"] = (
            aws_sdk_partnercentral_account.types.invitation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ConnectionInvitationSummary.status required")
    return out
