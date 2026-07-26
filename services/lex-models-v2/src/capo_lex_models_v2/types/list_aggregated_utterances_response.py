"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListAggregatedUtterancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.aggregated_utterances_summary_list
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.timestamp
    import capo_lex_models_v2.types.utterance_aggregation_duration


class ListAggregatedUtterancesResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contains the utterances.</p>"""
    bot_alias_id: NotRequired["capo_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The identifier of the bot alias that contains the utterances. If you specified the bot version, the bot alias ID isn't returned.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The identifier of the bot version that contains the utterances. If you specified the bot alias, the bot version isn't returned.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale that the utterances are in.</p>"""
    aggregation_duration: NotRequired[
        "capo_lex_models_v2.types.utterance_aggregation_duration.UtteranceAggregationDuration"
    ]
    """<p>The time period used to aggregate the utterance data.</p>"""
    aggregation_window_start_time: NotRequired[
        "capo_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the aggregation window begins. Only data collected after this time is returned in the results.</p>"""
    aggregation_window_end_time: NotRequired[
        "capo_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the aggregation window ends. Only data collected between the start time and the end time are returned in the results. </p>"""
    aggregation_last_refreshed_date_time: NotRequired[
        "capo_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The last date and time that the aggregated data was collected. The time period depends on the length of the aggregation window.</p> <ul> <li> <p> <b>Hours</b> - for 1 hour time window, every half hour; otherwise every hour.</p> </li> <li> <p> <b>Days</b> - every 6 hours</p> </li> <li> <p> <b>Weeks</b> - for a one week time window, every 12 hours; otherwise, every day</p> </li> </ul>"""
    aggregated_utterances_summaries: NotRequired[
        "capo_lex_models_v2.types.aggregated_utterances_summary_list.AggregatedUtterancesSummaryList"
    ]
    """<p>Summaries of the aggregated utterance data. Each response contains information about the number of times that the utterance was seen during the time period, whether it was detected or missed, and when it was seen during the time period.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListAggregatedUtterances</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListAggregatedUtterances</code> operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAggregatedUtterancesResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "aggregation_duration" in value:
        import capo_lex_models_v2.types.utterance_aggregation_duration

        out["aggregationDuration"] = (
            capo_lex_models_v2.types.utterance_aggregation_duration.serialize_json(
                value["aggregation_duration"]
            )
        )
    if "aggregation_window_start_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["aggregationWindowStartTime"] = (
            capo_lex_models_v2.types.timestamp.serialize_json(
                value["aggregation_window_start_time"]
            )
        )
    if "aggregation_window_end_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["aggregationWindowEndTime"] = (
            capo_lex_models_v2.types.timestamp.serialize_json(
                value["aggregation_window_end_time"]
            )
        )
    if "aggregation_last_refreshed_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["aggregationLastRefreshedDateTime"] = (
            capo_lex_models_v2.types.timestamp.serialize_json(
                value["aggregation_last_refreshed_date_time"]
            )
        )
    if "aggregated_utterances_summaries" in value:
        import capo_lex_models_v2.types.aggregated_utterances_summary_list

        out["aggregatedUtterancesSummaries"] = (
            capo_lex_models_v2.types.aggregated_utterances_summary_list.serialize_json(
                value["aggregated_utterances_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAggregatedUtterancesResponse:
    out: ListAggregatedUtterancesResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "aggregationDuration" in data:
        import capo_lex_models_v2.types.utterance_aggregation_duration

        out["aggregation_duration"] = (
            capo_lex_models_v2.types.utterance_aggregation_duration.deserialize_json(
                data["aggregationDuration"]
            )
        )
    if "aggregationWindowStartTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["aggregation_window_start_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["aggregationWindowStartTime"]
            )
        )
    if "aggregationWindowEndTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["aggregation_window_end_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["aggregationWindowEndTime"]
            )
        )
    if "aggregationLastRefreshedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["aggregation_last_refreshed_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["aggregationLastRefreshedDateTime"]
            )
        )
    if "aggregatedUtterancesSummaries" in data:
        import capo_lex_models_v2.types.aggregated_utterances_summary_list

        out["aggregated_utterances_summaries"] = (
            capo_lex_models_v2.types.aggregated_utterances_summary_list.deserialize_json(
                data["aggregatedUtterancesSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
