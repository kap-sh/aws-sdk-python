"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceAggregationDuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.relative_aggregation_duration


class UtteranceAggregationDuration(TypedDict, closed=True):
    relative_aggregation_duration: "aws_sdk_lex_models_v2.types.relative_aggregation_duration.RelativeAggregationDuration"
    """<p>The desired time window for aggregating utterances. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceAggregationDuration) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.relative_aggregation_duration

    out["relativeAggregationDuration"] = (
        aws_sdk_lex_models_v2.types.relative_aggregation_duration.serialize_json(
            value["relative_aggregation_duration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UtteranceAggregationDuration:
    out: UtteranceAggregationDuration = {}  # type: ignore[typeddict-item]
    if "relativeAggregationDuration" in data:
        import aws_sdk_lex_models_v2.types.relative_aggregation_duration

        out["relative_aggregation_duration"] = (
            aws_sdk_lex_models_v2.types.relative_aggregation_duration.deserialize_json(
                data["relativeAggregationDuration"]
            )
        )
    else:
        raise DeserializationError(
            "UtteranceAggregationDuration.relative_aggregation_duration required"
        )
    return out
