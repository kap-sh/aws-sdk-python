"""Generated from Smithy shape ``com.amazonaws.inspector2#DateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class DateFilter(TypedDict, closed=True):
    start_inclusive: NotRequired["datetime.datetime"]
    """<p>A timestamp representing the start of the time period filtered on.</p>"""
    end_inclusive: NotRequired["datetime.datetime"]
    """<p>A timestamp representing the end of the time period filtered on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateFilter) -> dict:
    out: dict = {}
    if "start_inclusive" in value:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["startInclusive"] = (
            aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
                value["start_inclusive"]
            )
        )
    if "end_inclusive" in value:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["endInclusive"] = (
            aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
                value["end_inclusive"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateFilter:
    out: DateFilter = {}  # type: ignore[typeddict-item]
    if "startInclusive" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["start_inclusive"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["startInclusive"]
            )
        )
    if "endInclusive" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["end_inclusive"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["endInclusive"]
            )
        )
    return out
