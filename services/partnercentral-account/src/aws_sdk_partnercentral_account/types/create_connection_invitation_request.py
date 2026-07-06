"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CreateConnectionInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.connection_type
    import aws_sdk_partnercentral_account.types.email
    import aws_sdk_partnercentral_account.types.participant_identifier
    import aws_sdk_partnercentral_account.types.sensitive_unicode_string
    import aws_sdk_partnercentral_account.types.unicode_string_including_new_line


class CreateConnectionInvitationRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection invitation will be created.</p>"""
    client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    connection_type: (
        "aws_sdk_partnercentral_account.types.connection_type.ConnectionType"
    )
    """<p>The type of connection being requested (e.g., reseller, distributor, technology partner).</p>"""
    email: "aws_sdk_partnercentral_account.types.email.Email"
    """<p>The email address of the person to send the connection invitation to.</p>"""
    message: "aws_sdk_partnercentral_account.types.unicode_string_including_new_line.UnicodeStringIncludingNewLine"
    """<p>A custom message to include with the connection invitation.</p>"""
    name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The name of the person sending the connection invitation.</p>"""
    receiver_identifier: "aws_sdk_partnercentral_account.types.participant_identifier.ParticipantIdentifier"
    """<p>The identifier of the organization or partner to invite for connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionInvitationRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    import aws_sdk_partnercentral_account.types.connection_type

    out["ConnectionType"] = (
        aws_sdk_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
            value["connection_type"]
        )
    )
    out["Email"] = value["email"]
    out["Message"] = value["message"]
    out["Name"] = value["name"]
    out["ReceiverIdentifier"] = value["receiver_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionInvitationRequest:
    out: CreateConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CreateConnectionInvitationRequest.catalog required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateConnectionInvitationRequest.client_token required"
        )
    if "ConnectionType" in data:
        import aws_sdk_partnercentral_account.types.connection_type

        out["connection_type"] = (
            aws_sdk_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                data["ConnectionType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectionInvitationRequest.connection_type required"
        )
    if "Email" in data:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("CreateConnectionInvitationRequest.email required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("CreateConnectionInvitationRequest.message required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateConnectionInvitationRequest.name required")
    if "ReceiverIdentifier" in data:
        out["receiver_identifier"] = data["ReceiverIdentifier"]
    else:
        raise DeserializationError(
            "CreateConnectionInvitationRequest.receiver_identifier required"
        )
    return out
