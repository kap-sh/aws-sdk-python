"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListRelationshipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.account_id_list
    import aws_sdk_partnercentral_channel.types.association_type_list
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.list_relationships_sort_base
    import aws_sdk_partnercentral_channel.types.next_token
    import aws_sdk_partnercentral_channel.types.program_management_account_identifier_list
    import aws_sdk_partnercentral_channel.types.relationship_display_name_list


class ListRelationshipsRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier to filter relationships.</p>"""
    max_results: "int"
    """<p>The maximum number of results to return in a single call.</p>"""
    associated_account_ids: NotRequired[
        "aws_sdk_partnercentral_channel.types.account_id_list.AccountIdList"
    ]
    """<p>Filter by associated AWS account IDs.</p>"""
    association_types: NotRequired[
        "aws_sdk_partnercentral_channel.types.association_type_list.AssociationTypeList"
    ]
    """<p>Filter by association types.</p>"""
    display_names: NotRequired[
        "aws_sdk_partnercentral_channel.types.relationship_display_name_list.RelationshipDisplayNameList"
    ]
    """<p>Filter by display names.</p>"""
    program_management_account_identifiers: NotRequired[
        "aws_sdk_partnercentral_channel.types.program_management_account_identifier_list.ProgramManagementAccountIdentifierList"
    ]
    """<p>Filter by program management account identifiers.</p>"""
    sort: NotRequired[
        "aws_sdk_partnercentral_channel.types.list_relationships_sort_base.ListRelationshipsSortBase"
    ]
    """<p>Sorting options for the results.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_channel.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRelationshipsRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["maxResults"] = value.get("max_results", 20)
    if "associated_account_ids" in value:
        import aws_sdk_partnercentral_channel.types.account_id_list

        out["associatedAccountIds"] = (
            aws_sdk_partnercentral_channel.types.account_id_list.serialize_aws_json_1_0(
                value["associated_account_ids"]
            )
        )
    if "association_types" in value:
        import aws_sdk_partnercentral_channel.types.association_type_list

        out["associationTypes"] = (
            aws_sdk_partnercentral_channel.types.association_type_list.serialize_aws_json_1_0(
                value["association_types"]
            )
        )
    if "display_names" in value:
        import aws_sdk_partnercentral_channel.types.relationship_display_name_list

        out["displayNames"] = (
            aws_sdk_partnercentral_channel.types.relationship_display_name_list.serialize_aws_json_1_0(
                value["display_names"]
            )
        )
    if "program_management_account_identifiers" in value:
        import aws_sdk_partnercentral_channel.types.program_management_account_identifier_list

        out["programManagementAccountIdentifiers"] = (
            aws_sdk_partnercentral_channel.types.program_management_account_identifier_list.serialize_aws_json_1_0(
                value["program_management_account_identifiers"]
            )
        )
    if "sort" in value:
        import aws_sdk_partnercentral_channel.types.list_relationships_sort_base

        out["sort"] = (
            aws_sdk_partnercentral_channel.types.list_relationships_sort_base.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRelationshipsRequest:
    out: ListRelationshipsRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("ListRelationshipsRequest.catalog required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 20
    if "associatedAccountIds" in data:
        import aws_sdk_partnercentral_channel.types.account_id_list

        out["associated_account_ids"] = (
            aws_sdk_partnercentral_channel.types.account_id_list.deserialize_aws_json_1_0(
                data["associatedAccountIds"]
            )
        )
    if "associationTypes" in data:
        import aws_sdk_partnercentral_channel.types.association_type_list

        out["association_types"] = (
            aws_sdk_partnercentral_channel.types.association_type_list.deserialize_aws_json_1_0(
                data["associationTypes"]
            )
        )
    if "displayNames" in data:
        import aws_sdk_partnercentral_channel.types.relationship_display_name_list

        out["display_names"] = (
            aws_sdk_partnercentral_channel.types.relationship_display_name_list.deserialize_aws_json_1_0(
                data["displayNames"]
            )
        )
    if "programManagementAccountIdentifiers" in data:
        import aws_sdk_partnercentral_channel.types.program_management_account_identifier_list

        out["program_management_account_identifiers"] = (
            aws_sdk_partnercentral_channel.types.program_management_account_identifier_list.deserialize_aws_json_1_0(
                data["programManagementAccountIdentifiers"]
            )
        )
    if "sort" in data:
        import aws_sdk_partnercentral_channel.types.list_relationships_sort_base

        out["sort"] = (
            aws_sdk_partnercentral_channel.types.list_relationships_sort_base.deserialize_aws_json_1_0(
                data["sort"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
