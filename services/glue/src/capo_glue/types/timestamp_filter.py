"""Generated from Smithy shape ``com.amazonaws.glue#TimestampFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.timestamp


class TimestampFilter(TypedDict, closed=True):
    recorded_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The timestamp before which statistics should be included in the results.</p>"""
    recorded_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The timestamp after which statistics should be included in the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampFilter) -> dict:
    out: dict = {}
    if "recorded_before" in value:
        import capo_glue.types.timestamp

        out["RecordedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["recorded_before"]
        )
    if "recorded_after" in value:
        import capo_glue.types.timestamp

        out["RecordedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["recorded_after"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimestampFilter:
    out: TimestampFilter = {}  # type: ignore[typeddict-item]
    if "RecordedBefore" in data:
        import capo_glue.types.timestamp

        out["recorded_before"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["RecordedBefore"]
        )
    if "RecordedAfter" in data:
        import capo_glue.types.timestamp

        out["recorded_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["RecordedAfter"]
        )
    return out
