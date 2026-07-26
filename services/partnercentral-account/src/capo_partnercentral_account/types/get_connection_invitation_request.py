"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetConnectionInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_invitation_id


class GetConnectionInvitationRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection invitation exists.</p>"""
    identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId"
    """<p>The unique identifier of the connection invitation to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionInvitationRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionInvitationRequest:
    out: GetConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetConnectionInvitationRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetConnectionInvitationRequest.identifier required")
    return out
