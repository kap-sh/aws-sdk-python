"""Generated from Smithy shape ``com.amazonaws.datazone#ListTimeSeriesDataPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_identifier
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token
    import capo_datazone.types.time_series_entity_type
    import capo_datazone.types.time_series_form_name


class ListTimeSeriesDataPointsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain that houses the assets for which you want to list time series data points.</p>"""
    entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset for which you want to list data points.</p>"""
    entity_type: "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType"
    """<p>The type of the asset for which you want to list data points.</p>"""
    form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series data points form.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the data points that you want to list started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the data points that you wanted to list ended.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of data points is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of data points, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of data points to return in a single call to ListTimeSeriesDataPoints. When the number of data points to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTimeSeriesDataPointsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTimeSeriesDataPointsInput:
    out: ListTimeSeriesDataPointsInput = {}  # type: ignore[typeddict-item]
    return out
