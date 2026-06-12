"""Generated from Smithy shape ``com.amazonaws.devopsguru#SearchOrganizationInsightsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.insight_type
    import aws_sdk_devops_guru.types.search_insights_account_id_list
    import aws_sdk_devops_guru.types.search_organization_insights_filters
    import aws_sdk_devops_guru.types.search_organization_insights_max_results
    import aws_sdk_devops_guru.types.start_time_range
    import aws_sdk_devops_guru.types.uuid_next_token


class SearchOrganizationInsightsRequest(TypedDict):
    account_ids: "aws_sdk_devops_guru.types.search_insights_account_id_list.SearchInsightsAccountIdList"
    """<p>The ID of the Amazon Web Services account. </p>"""
    start_time_range: "aws_sdk_devops_guru.types.start_time_range.StartTimeRange"
    filters: NotRequired[
        "aws_sdk_devops_guru.types.search_organization_insights_filters.SearchOrganizationInsightsFilters"
    ]
    """<p> A <code>SearchOrganizationInsightsFilters</code> object that is used to set the severity and status filters on your insight search. </p>"""
    max_results: NotRequired[
        "aws_sdk_devops_guru.types.search_organization_insights_max_results.SearchOrganizationInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    type: "aws_sdk_devops_guru.types.insight_type.InsightType"
    """<p> The type of insights you are searching for (<code>REACTIVE</code> or <code>PROACTIVE</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchOrganizationInsightsRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.search_insights_account_id_list

    out["AccountIds"] = (
        aws_sdk_devops_guru.types.search_insights_account_id_list.serialize_json(
            value["account_ids"]
        )
    )
    import aws_sdk_devops_guru.types.start_time_range

    out["StartTimeRange"] = aws_sdk_devops_guru.types.start_time_range.serialize_json(
        value["start_time_range"]
    )
    if "filters" in value:
        import aws_sdk_devops_guru.types.search_organization_insights_filters

        out["Filters"] = (
            aws_sdk_devops_guru.types.search_organization_insights_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_devops_guru.types.insight_type

    out["Type"] = aws_sdk_devops_guru.types.insight_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SearchOrganizationInsightsRequest:
    out: SearchOrganizationInsightsRequest = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_devops_guru.types.search_insights_account_id_list

        out["account_ids"] = (
            aws_sdk_devops_guru.types.search_insights_account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    else:
        raise DeserializationError(
            "SearchOrganizationInsightsRequest.account_ids required"
        )
    if "StartTimeRange" in data:
        import aws_sdk_devops_guru.types.start_time_range

        out["start_time_range"] = (
            aws_sdk_devops_guru.types.start_time_range.deserialize_json(
                data["StartTimeRange"]
            )
        )
    else:
        raise DeserializationError(
            "SearchOrganizationInsightsRequest.start_time_range required"
        )
    if "Filters" in data:
        import aws_sdk_devops_guru.types.search_organization_insights_filters

        out["filters"] = (
            aws_sdk_devops_guru.types.search_organization_insights_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Type" in data:
        import aws_sdk_devops_guru.types.insight_type

        out["type"] = aws_sdk_devops_guru.types.insight_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("SearchOrganizationInsightsRequest.type required")
    return out
