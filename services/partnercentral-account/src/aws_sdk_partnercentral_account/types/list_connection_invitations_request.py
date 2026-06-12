"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListConnectionInvitationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.connection_type
    import aws_sdk_partnercentral_account.types.invitation_status
    import aws_sdk_partnercentral_account.types.max_results
    import aws_sdk_partnercentral_account.types.next_token
    import aws_sdk_partnercentral_account.types.participant_identifier_list
    import aws_sdk_partnercentral_account.types.participant_type


class ListConnectionInvitationsRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results in paginated responses.</p>"""
    connection_type: NotRequired[
        "aws_sdk_partnercentral_account.types.connection_type.ConnectionType"
    ]
    """<p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>"""
    max_results: "aws_sdk_partnercentral_account.types.max_results.MaxResults"
    """<p>The maximum number of connection invitations to return in a single response.</p>"""
    other_participant_identifiers: NotRequired[
        "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
    ]
    """<p>Filter results by specific participant identifiers.</p>"""
    participant_type: NotRequired[
        "aws_sdk_partnercentral_account.types.participant_type.ParticipantType"
    ]
    """<p>Filter results by participant type (inviter or invitee).</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_account.types.invitation_status.InvitationStatus"
    ]
    """<p>Filter results by invitation status (pending, accepted, rejected, canceled, expired).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionInvitationsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "connection_type" in value:
        import aws_sdk_partnercentral_account.types.connection_type

        out["ConnectionType"] = (
            aws_sdk_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
                value["connection_type"]
            )
        )
    out["MaxResults"] = value.get("max_results", 20)
    if "other_participant_identifiers" in value:
        import aws_sdk_partnercentral_account.types.participant_identifier_list

        out["OtherParticipantIdentifiers"] = (
            aws_sdk_partnercentral_account.types.participant_identifier_list.serialize_aws_json_1_0(
                value["other_participant_identifiers"]
            )
        )
    if "participant_type" in value:
        import aws_sdk_partnercentral_account.types.participant_type

        out["ParticipantType"] = (
            aws_sdk_partnercentral_account.types.participant_type.serialize_aws_json_1_0(
                value["participant_type"]
            )
        )
    if "status" in value:
        import aws_sdk_partnercentral_account.types.invitation_status

        out["Status"] = (
            aws_sdk_partnercentral_account.types.invitation_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionInvitationsRequest:
    out: ListConnectionInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListConnectionInvitationsRequest.catalog required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ConnectionType" in data:
        import aws_sdk_partnercentral_account.types.connection_type

        out["connection_type"] = (
            aws_sdk_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                data["ConnectionType"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 20
    if "OtherParticipantIdentifiers" in data:
        import aws_sdk_partnercentral_account.types.participant_identifier_list

        out["other_participant_identifiers"] = (
            aws_sdk_partnercentral_account.types.participant_identifier_list.deserialize_aws_json_1_0(
                data["OtherParticipantIdentifiers"]
            )
        )
    if "ParticipantType" in data:
        import aws_sdk_partnercentral_account.types.participant_type

        out["participant_type"] = (
            aws_sdk_partnercentral_account.types.participant_type.deserialize_aws_json_1_0(
                data["ParticipantType"]
            )
        )
    if "Status" in data:
        import aws_sdk_partnercentral_account.types.invitation_status

        out["status"] = (
            aws_sdk_partnercentral_account.types.invitation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
