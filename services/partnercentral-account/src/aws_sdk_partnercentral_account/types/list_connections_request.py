"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListConnectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.connection_type_filter
    import aws_sdk_partnercentral_account.types.max_results
    import aws_sdk_partnercentral_account.types.next_token
    import aws_sdk_partnercentral_account.types.participant_identifier_list


class ListConnectionsRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results in paginated responses.</p>"""
    connection_type: NotRequired[
        "aws_sdk_partnercentral_account.types.connection_type_filter.ConnectionTypeFilter"
    ]
    """<p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>"""
    max_results: "aws_sdk_partnercentral_account.types.max_results.MaxResults"
    """<p>The maximum number of connections to return in a single response.</p>"""
    other_participant_identifiers: NotRequired[
        "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
    ]
    """<p>Filter results by specific participant identifiers.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "connection_type" in value:
        out["ConnectionType"] = value["connection_type"]
    out["MaxResults"] = value.get("max_results", 20)
    if "other_participant_identifiers" in value:
        import aws_sdk_partnercentral_account.types.participant_identifier_list

        out["OtherParticipantIdentifiers"] = (
            aws_sdk_partnercentral_account.types.participant_identifier_list.serialize_aws_json_1_0(
                value["other_participant_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsRequest:
    out: ListConnectionsRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListConnectionsRequest.catalog required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
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
    return out
