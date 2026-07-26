"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListUtteranceAnalyticsDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_utterance_filters
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.timestamp
    import capo_lex_models_v2.types.utterance_data_sort_by


class ListUtteranceAnalyticsDataRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier for the bot for which you want to retrieve utterance analytics.</p>"""
    start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The date and time that marks the beginning of the range of time for which you want to see utterance analytics.</p>"""
    end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The date and time that marks the end of the range of time for which you want to see utterance analytics.</p>"""
    sort_by: NotRequired[
        "capo_lex_models_v2.types.utterance_data_sort_by.UtteranceDataSortBy"
    ]
    """<p>An object specifying the measure and method by which to sort the utterance analytics data.</p>"""
    filters: NotRequired[
        "capo_lex_models_v2.types.analytics_utterance_filters.AnalyticsUtteranceFilters"
    ]
    """<p>A list of objects, each of which describes a condition by which you want to filter the results.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListUtteranceAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListUtteranceAnalyticsData request to return the next page of results. For a complete set of results, call the ListUtteranceAnalyticsData operation until the nextToken returned in the response is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUtteranceAnalyticsDataRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.timestamp

    out["startDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["start_date_time"]
    )
    import capo_lex_models_v2.types.timestamp

    out["endDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["end_date_time"]
    )
    if "sort_by" in value:
        import capo_lex_models_v2.types.utterance_data_sort_by

        out["sortBy"] = capo_lex_models_v2.types.utterance_data_sort_by.serialize_json(
            value["sort_by"]
        )
    if "filters" in value:
        import capo_lex_models_v2.types.analytics_utterance_filters

        out["filters"] = (
            capo_lex_models_v2.types.analytics_utterance_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUtteranceAnalyticsDataRequest:
    out: ListUtteranceAnalyticsDataRequest = {}  # type: ignore[typeddict-item]
    if "startDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["start_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["startDateTime"]
        )
    else:
        raise DeserializationError(
            "ListUtteranceAnalyticsDataRequest.start_date_time required"
        )
    if "endDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["end_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["endDateTime"]
        )
    else:
        raise DeserializationError(
            "ListUtteranceAnalyticsDataRequest.end_date_time required"
        )
    if "sortBy" in data:
        import capo_lex_models_v2.types.utterance_data_sort_by

        out["sort_by"] = (
            capo_lex_models_v2.types.utterance_data_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if "filters" in data:
        import capo_lex_models_v2.types.analytics_utterance_filters

        out["filters"] = (
            capo_lex_models_v2.types.analytics_utterance_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
