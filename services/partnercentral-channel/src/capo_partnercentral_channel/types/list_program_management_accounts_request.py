"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListProgramManagementAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id_list
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.list_program_management_accounts_sort_base
    import capo_partnercentral_channel.types.next_token
    import capo_partnercentral_channel.types.program_list
    import capo_partnercentral_channel.types.program_management_account_display_name_list
    import capo_partnercentral_channel.types.program_management_account_status_list


class ListProgramManagementAccountsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier to filter accounts.</p>"""
    max_results: "int"
    """<p>The maximum number of results to return in a single call.</p>"""
    display_names: NotRequired[
        "capo_partnercentral_channel.types.program_management_account_display_name_list.ProgramManagementAccountDisplayNameList"
    ]
    """<p>Filter by display names.</p>"""
    programs: NotRequired["capo_partnercentral_channel.types.program_list.ProgramList"]
    """<p>Filter by program types.</p>"""
    account_ids: NotRequired[
        "capo_partnercentral_channel.types.account_id_list.AccountIdList"
    ]
    """<p>Filter by AWS account IDs.</p>"""
    statuses: NotRequired[
        "capo_partnercentral_channel.types.program_management_account_status_list.ProgramManagementAccountStatusList"
    ]
    """<p>Filter by program management account statuses.</p>"""
    sort: NotRequired[
        "capo_partnercentral_channel.types.list_program_management_accounts_sort_base.ListProgramManagementAccountsSortBase"
    ]
    """<p>Sorting options for the results.</p>"""
    next_token: NotRequired["capo_partnercentral_channel.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProgramManagementAccountsRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["maxResults"] = value.get("max_results", 20)
    if "display_names" in value:
        import capo_partnercentral_channel.types.program_management_account_display_name_list

        out["displayNames"] = (
            capo_partnercentral_channel.types.program_management_account_display_name_list.serialize_aws_json_1_0(
                value["display_names"]
            )
        )
    if "programs" in value:
        import capo_partnercentral_channel.types.program_list

        out["programs"] = (
            capo_partnercentral_channel.types.program_list.serialize_aws_json_1_0(
                value["programs"]
            )
        )
    if "account_ids" in value:
        import capo_partnercentral_channel.types.account_id_list

        out["accountIds"] = (
            capo_partnercentral_channel.types.account_id_list.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "statuses" in value:
        import capo_partnercentral_channel.types.program_management_account_status_list

        out["statuses"] = (
            capo_partnercentral_channel.types.program_management_account_status_list.serialize_aws_json_1_0(
                value["statuses"]
            )
        )
    if "sort" in value:
        import capo_partnercentral_channel.types.list_program_management_accounts_sort_base

        out["sort"] = (
            capo_partnercentral_channel.types.list_program_management_accounts_sort_base.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProgramManagementAccountsRequest:
    out: ListProgramManagementAccountsRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError(
            "ListProgramManagementAccountsRequest.catalog required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 20
    if "displayNames" in data:
        import capo_partnercentral_channel.types.program_management_account_display_name_list

        out["display_names"] = (
            capo_partnercentral_channel.types.program_management_account_display_name_list.deserialize_aws_json_1_0(
                data["displayNames"]
            )
        )
    if "programs" in data:
        import capo_partnercentral_channel.types.program_list

        out["programs"] = (
            capo_partnercentral_channel.types.program_list.deserialize_aws_json_1_0(
                data["programs"]
            )
        )
    if "accountIds" in data:
        import capo_partnercentral_channel.types.account_id_list

        out["account_ids"] = (
            capo_partnercentral_channel.types.account_id_list.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if "statuses" in data:
        import capo_partnercentral_channel.types.program_management_account_status_list

        out["statuses"] = (
            capo_partnercentral_channel.types.program_management_account_status_list.deserialize_aws_json_1_0(
                data["statuses"]
            )
        )
    if "sort" in data:
        import capo_partnercentral_channel.types.list_program_management_accounts_sort_base

        out["sort"] = (
            capo_partnercentral_channel.types.list_program_management_accounts_sort_base.deserialize_aws_json_1_0(
                data["sort"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
