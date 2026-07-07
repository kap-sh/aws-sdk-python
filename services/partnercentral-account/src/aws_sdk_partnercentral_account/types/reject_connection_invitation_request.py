"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#RejectConnectionInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.connection_invitation_id


class RejectConnectionInvitationRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection invitation exists.</p>"""
    identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId"
    """<p>The unique identifier of the connection invitation to reject.</p>"""
    client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    reason: NotRequired["str"]
    """<p>The reason for rejecting the connection invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectConnectionInvitationRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    out["ClientToken"] = value["client_token"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectConnectionInvitationRequest:
    out: RejectConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("RejectConnectionInvitationRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "RejectConnectionInvitationRequest.identifier required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "RejectConnectionInvitationRequest.client_token required"
        )
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
