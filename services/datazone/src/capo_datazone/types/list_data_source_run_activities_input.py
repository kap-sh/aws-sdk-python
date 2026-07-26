"""Generated from Smithy shape ``com.amazonaws.datazone#ListDataSourceRunActivitiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_asset_activity_status
    import capo_datazone.types.data_source_run_id
    import capo_datazone.types.domain_id
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token


class ListDataSourceRunActivitiesInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which to list data source run activities.</p>"""
    identifier: "capo_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The identifier of the data source run.</p>"""
    status: NotRequired[
        "capo_datazone.types.data_asset_activity_status.DataAssetActivityStatus"
    ]
    """<p>The status of the data source run.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of activities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of activities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRunActivities</code> to list the next set of activities.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of activities to return in a single call to <code>ListDataSourceRunActivities</code>. When the number of activities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRunActivities</code> to list the next set of activities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourceRunActivitiesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSourceRunActivitiesInput:
    out: ListDataSourceRunActivitiesInput = {}  # type: ignore[typeddict-item]
    return out
