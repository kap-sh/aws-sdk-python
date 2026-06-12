"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListOrganizationInsightsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.list_insights_account_id_list
    import aws_sdk_devops_guru.types.list_insights_max_results
    import aws_sdk_devops_guru.types.list_insights_organizational_unit_id_list
    import aws_sdk_devops_guru.types.list_insights_status_filter
    import aws_sdk_devops_guru.types.uuid_next_token


class ListOrganizationInsightsRequest(TypedDict):
    status_filter: (
        "aws_sdk_devops_guru.types.list_insights_status_filter.ListInsightsStatusFilter"
    )
    max_results: NotRequired[
        "aws_sdk_devops_guru.types.list_insights_max_results.ListInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    account_ids: NotRequired[
        "aws_sdk_devops_guru.types.list_insights_account_id_list.ListInsightsAccountIdList"
    ]
    """<p>The ID of the Amazon Web Services account. </p>"""
    organizational_unit_ids: NotRequired[
        "aws_sdk_devops_guru.types.list_insights_organizational_unit_id_list.ListInsightsOrganizationalUnitIdList"
    ]
    """<p>The ID of the organizational unit.</p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationInsightsRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.list_insights_status_filter

    out["StatusFilter"] = (
        aws_sdk_devops_guru.types.list_insights_status_filter.serialize_json(
            value["status_filter"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "account_ids" in value:
        import aws_sdk_devops_guru.types.list_insights_account_id_list

        out["AccountIds"] = (
            aws_sdk_devops_guru.types.list_insights_account_id_list.serialize_json(
                value["account_ids"]
            )
        )
    if "organizational_unit_ids" in value:
        import aws_sdk_devops_guru.types.list_insights_organizational_unit_id_list

        out["OrganizationalUnitIds"] = (
            aws_sdk_devops_guru.types.list_insights_organizational_unit_id_list.serialize_json(
                value["organizational_unit_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrganizationInsightsRequest:
    out: ListOrganizationInsightsRequest = {}  # type: ignore[typeddict-item]
    if "StatusFilter" in data:
        import aws_sdk_devops_guru.types.list_insights_status_filter

        out["status_filter"] = (
            aws_sdk_devops_guru.types.list_insights_status_filter.deserialize_json(
                data["StatusFilter"]
            )
        )
    else:
        raise DeserializationError(
            "ListOrganizationInsightsRequest.status_filter required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "AccountIds" in data:
        import aws_sdk_devops_guru.types.list_insights_account_id_list

        out["account_ids"] = (
            aws_sdk_devops_guru.types.list_insights_account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    if "OrganizationalUnitIds" in data:
        import aws_sdk_devops_guru.types.list_insights_organizational_unit_id_list

        out["organizational_unit_ids"] = (
            aws_sdk_devops_guru.types.list_insights_organizational_unit_id_list.deserialize_json(
                data["OrganizationalUnitIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
