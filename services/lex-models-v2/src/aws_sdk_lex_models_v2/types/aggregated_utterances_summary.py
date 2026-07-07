"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.hit_count
    import aws_sdk_lex_models_v2.types.missed_count
    import aws_sdk_lex_models_v2.types.timestamp
    import aws_sdk_lex_models_v2.types.utterance


class AggregatedUtterancesSummary(TypedDict, closed=True):
    utterance: NotRequired["aws_sdk_lex_models_v2.types.utterance.Utterance"]
    """<p>The text of the utterance. If the utterance was used with the <code>RecognizeUtterance</code> operation, the text is the transcription of the audio utterance.</p>"""
    hit_count: NotRequired["aws_sdk_lex_models_v2.types.hit_count.HitCount"]
    """<p>The number of times that the utterance was detected by Amazon Lex during the time period. When an utterance is detected, it activates an intent or a slot.</p>"""
    missed_count: NotRequired["aws_sdk_lex_models_v2.types.missed_count.MissedCount"]
    """<p>The number of times that the utterance was missed by Amazon Lex An utterance is missed when it doesn't activate an intent or slot.</p>"""
    utterance_first_recorded_in_aggregation_duration: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the utterance was first recorded in the time window for aggregation. An utterance may have been sent to Amazon Lex before that time, but only utterances within the time window are counted.</p>"""
    utterance_last_recorded_in_aggregation_duration: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The last date and time that an utterance was recorded in the time window for aggregation. An utterance may be sent to Amazon Lex after that time, but only utterances within the time window are counted.</p>"""
    contains_data_from_deleted_resources: NotRequired[
        "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Aggregated utterance data may contain utterances from versions of your bot that have since been deleted. When the aggregated contains this kind of data, this field is set to true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedUtterancesSummary) -> dict:
    out: dict = {}
    if "utterance" in value:
        out["utterance"] = value["utterance"]
    if "hit_count" in value:
        out["hitCount"] = value["hit_count"]
    if "missed_count" in value:
        out["missedCount"] = value["missed_count"]
    if "utterance_first_recorded_in_aggregation_duration" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["utteranceFirstRecordedInAggregationDuration"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["utterance_first_recorded_in_aggregation_duration"]
            )
        )
    if "utterance_last_recorded_in_aggregation_duration" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["utteranceLastRecordedInAggregationDuration"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["utterance_last_recorded_in_aggregation_duration"]
            )
        )
    if "contains_data_from_deleted_resources" in value:
        out["containsDataFromDeletedResources"] = value[
            "contains_data_from_deleted_resources"
        ]
    return out


def deserialize_json(data: dict) -> AggregatedUtterancesSummary:
    out: AggregatedUtterancesSummary = {}  # type: ignore[typeddict-item]
    if "utterance" in data:
        out["utterance"] = data["utterance"]
    if "hitCount" in data:
        out["hit_count"] = data["hitCount"]
    if "missedCount" in data:
        out["missed_count"] = data["missedCount"]
    if "utteranceFirstRecordedInAggregationDuration" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["utterance_first_recorded_in_aggregation_duration"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["utteranceFirstRecordedInAggregationDuration"]
            )
        )
    if "utteranceLastRecordedInAggregationDuration" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["utterance_last_recorded_in_aggregation_duration"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["utteranceLastRecordedInAggregationDuration"]
            )
        )
    if "containsDataFromDeletedResources" in data:
        out["contains_data_from_deleted_resources"] = data[
            "containsDataFromDeletedResources"
        ]
    return out
