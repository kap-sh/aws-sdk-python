"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DateRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.timestamp


class DateRangeFilter(TypedDict, closed=True):
    start_date_time: "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    """<p>A timestamp indicating the start date for the date range filter.</p>"""
    end_date_time: "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    """<p>A timestamp indicating the end date for the date range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateRangeFilter) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.timestamp

    out["startDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
        value["start_date_time"]
    )
    import aws_sdk_lex_models_v2.types.timestamp

    out["endDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
        value["end_date_time"]
    )
    return out


def deserialize_json(data: dict) -> DateRangeFilter:
    out: DateRangeFilter = {}  # type: ignore[typeddict-item]
    if "startDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["start_date_time"] = aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
            data["startDateTime"]
        )
    else:
        raise DeserializationError("DateRangeFilter.start_date_time required")
    if "endDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["end_date_time"] = aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
            data["endDateTime"]
        )
    else:
        raise DeserializationError("DateRangeFilter.end_date_time required")
    return out
