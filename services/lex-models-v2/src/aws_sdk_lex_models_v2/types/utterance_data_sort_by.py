"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceDataSortBy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_sort_order
    import aws_sdk_lex_models_v2.types.analytics_utterance_sort_by_name


class UtteranceDataSortBy(TypedDict):
    name: "aws_sdk_lex_models_v2.types.analytics_utterance_sort_by_name.AnalyticsUtteranceSortByName"
    """<p>The measure by which to sort the utterance analytics data.</p> <ul> <li> <p> <code>Count</code> – The number of utterances.</p> </li> <li> <p> <code>UtteranceTimestamp</code> – The date and time of the utterance.</p> </li> </ul>"""
    order: "aws_sdk_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceDataSortBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_utterance_sort_by_name

    out["name"] = (
        aws_sdk_lex_models_v2.types.analytics_utterance_sort_by_name.serialize_json(
            value["name"]
        )
    )
    import aws_sdk_lex_models_v2.types.analytics_sort_order

    out["order"] = aws_sdk_lex_models_v2.types.analytics_sort_order.serialize_json(
        value["order"]
    )
    return out


def deserialize_json(data: dict) -> UtteranceDataSortBy:
    out: UtteranceDataSortBy = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_sort_by_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_sort_by_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("UtteranceDataSortBy.name required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.analytics_sort_order

        out["order"] = (
            aws_sdk_lex_models_v2.types.analytics_sort_order.deserialize_json(
                data["order"]
            )
        )
    else:
        raise DeserializationError("UtteranceDataSortBy.order required")
    return out
