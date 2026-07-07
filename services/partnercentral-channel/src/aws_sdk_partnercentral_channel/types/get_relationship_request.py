"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#GetRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.program_management_account_identifier
    import aws_sdk_partnercentral_channel.types.relationship_identifier


class GetRelationshipRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the relationship.</p>"""
    program_management_account_identifier: "aws_sdk_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account associated with the relationship.</p>"""
    identifier: "aws_sdk_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier"
    """<p>The unique identifier of the relationship to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRelationshipRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRelationshipRequest:
    out: GetRelationshipRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("GetRelationshipRequest.catalog required")
    if "programManagementAccountIdentifier" in data:
        out["program_management_account_identifier"] = data[
            "programManagementAccountIdentifier"
        ]
    else:
        raise DeserializationError(
            "GetRelationshipRequest.program_management_account_identifier required"
        )
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("GetRelationshipRequest.identifier required")
    return out
