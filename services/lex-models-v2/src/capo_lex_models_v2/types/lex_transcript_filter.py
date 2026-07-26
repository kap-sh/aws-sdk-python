"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#LexTranscriptFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.date_range_filter


class LexTranscriptFilter(TypedDict, closed=True):
    date_range_filter: NotRequired[
        "capo_lex_models_v2.types.date_range_filter.DateRangeFilter"
    ]
    """<p>The object that contains a date range filter that will be applied to the transcript. Specify this object if you want Amazon Lex to only read the files that are within the date range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexTranscriptFilter) -> dict:
    out: dict = {}
    if "date_range_filter" in value:
        import capo_lex_models_v2.types.date_range_filter

        out["dateRangeFilter"] = (
            capo_lex_models_v2.types.date_range_filter.serialize_json(
                value["date_range_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> LexTranscriptFilter:
    out: LexTranscriptFilter = {}  # type: ignore[typeddict-item]
    if "dateRangeFilter" in data:
        import capo_lex_models_v2.types.date_range_filter

        out["date_range_filter"] = (
            capo_lex_models_v2.types.date_range_filter.deserialize_json(
                data["dateRangeFilter"]
            )
        )
    return out
