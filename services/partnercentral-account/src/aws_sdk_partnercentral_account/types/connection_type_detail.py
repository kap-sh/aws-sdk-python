"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.aws_account_id
    import aws_sdk_partnercentral_account.types.connection_type_status
    import aws_sdk_partnercentral_account.types.date_time
    import aws_sdk_partnercentral_account.types.email
    import aws_sdk_partnercentral_account.types.participant
    import aws_sdk_partnercentral_account.types.sensitive_unicode_string


class ConnectionTypeDetail(TypedDict):
    created_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when this connection type was created.</p>"""
    inviter_email: "aws_sdk_partnercentral_account.types.email.Email"
    """<p>The email address of the person who initiated this connection type.</p>"""
    inviter_name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The name of the person who initiated this connection type.</p>"""
    status: "aws_sdk_partnercentral_account.types.connection_type_status.ConnectionTypeStatus"
    """<p>The current status of this connection type.</p>"""
    canceled_at: NotRequired["aws_sdk_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when this connection type was cancelled, if applicable.</p>"""
    canceled_by: NotRequired[
        "aws_sdk_partnercentral_account.types.aws_account_id.AwsAccountId"
    ]
    """<p>The AWS account ID of the participant who cancelled this connection type.</p>"""
    other_participant: "aws_sdk_partnercentral_account.types.participant.Participant"
    """<p>Information about the other participant in this connection type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionTypeDetail) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_account.types.date_time

    out["CreatedAt"] = (
        aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    out["InviterEmail"] = value["inviter_email"]
    out["InviterName"] = value["inviter_name"]
    import aws_sdk_partnercentral_account.types.connection_type_status

    out["Status"] = (
        aws_sdk_partnercentral_account.types.connection_type_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "canceled_at" in value:
        import aws_sdk_partnercentral_account.types.date_time

        out["CanceledAt"] = (
            aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["canceled_at"]
            )
        )
    if "canceled_by" in value:
        out["CanceledBy"] = value["canceled_by"]
    import aws_sdk_partnercentral_account.types.participant

    out["OtherParticipant"] = (
        aws_sdk_partnercentral_account.types.participant.serialize_aws_json_1_0(
            value["other_participant"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionTypeDetail:
    out: ConnectionTypeDetail = {}  # type: ignore[typeddict-item]
    if "CreatedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["created_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("ConnectionTypeDetail.created_at required")
    if "InviterEmail" in data:
        out["inviter_email"] = data["InviterEmail"]
    else:
        raise DeserializationError("ConnectionTypeDetail.inviter_email required")
    if "InviterName" in data:
        out["inviter_name"] = data["InviterName"]
    else:
        raise DeserializationError("ConnectionTypeDetail.inviter_name required")
    if "Status" in data:
        import aws_sdk_partnercentral_account.types.connection_type_status

        out["status"] = (
            aws_sdk_partnercentral_account.types.connection_type_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ConnectionTypeDetail.status required")
    if "CanceledAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["canceled_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CanceledAt"]
            )
        )
    if "CanceledBy" in data:
        out["canceled_by"] = data["CanceledBy"]
    if "OtherParticipant" in data:
        import aws_sdk_partnercentral_account.types.participant

        out["other_participant"] = (
            aws_sdk_partnercentral_account.types.participant.deserialize_aws_json_1_0(
                data["OtherParticipant"]
            )
        )
    else:
        raise DeserializationError("ConnectionTypeDetail.other_participant required")
    return out
