"""Generated from Smithy shape ``com.amazonaws.inspector#TimestampRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.timestamp


class TimestampRange(TypedDict, closed=True):
    begin_date: NotRequired["capo_inspector.types.timestamp.Timestamp"]
    """<p>The minimum value of the timestamp range.</p>"""
    end_date: NotRequired["capo_inspector.types.timestamp.Timestamp"]
    """<p>The maximum value of the timestamp range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampRange) -> dict:
    out: dict = {}
    if "begin_date" in value:
        import capo_inspector.types.timestamp

        out["beginDate"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
            value["begin_date"]
        )
    if "end_date" in value:
        import capo_inspector.types.timestamp

        out["endDate"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
            value["end_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimestampRange:
    out: TimestampRange = {}  # type: ignore[typeddict-item]
    if "beginDate" in data:
        import capo_inspector.types.timestamp

        out["begin_date"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["beginDate"]
        )
    if "endDate" in data:
        import capo_inspector.types.timestamp

        out["end_date"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["endDate"]
        )
    return out
