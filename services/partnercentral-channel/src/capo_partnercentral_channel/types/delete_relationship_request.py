"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#DeleteRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.relationship_identifier


class DeleteRelationshipRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the relationship.</p>"""
    identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier"
    """<p>The unique identifier of the relationship to delete.</p>"""
    program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account associated with the relationship.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRelationshipRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["identifier"] = value["identifier"]
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRelationshipRequest:
    out: DeleteRelationshipRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("DeleteRelationshipRequest.catalog required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("DeleteRelationshipRequest.identifier required")
    if "programManagementAccountIdentifier" in data:
        out["program_management_account_identifier"] = data[
            "programManagementAccountIdentifier"
        ]
    else:
        raise DeserializationError(
            "DeleteRelationshipRequest.program_management_account_identifier required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
