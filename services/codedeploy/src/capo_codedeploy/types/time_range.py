"""Generated from Smithy shape ``com.amazonaws.codedeploy#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.timestamp


class TimeRange(TypedDict, closed=True):
    start: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>The start time of the time range.</p> <note> <p>Specify null to leave the start time open-ended.</p> </note>"""
    end: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>The end time of the time range.</p> <note> <p>Specify null to leave the end time open-ended.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeRange) -> dict:
    out: dict = {}
    if "start" in value:
        import capo_codedeploy.types.timestamp

        out["start"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["start"]
        )
    if "end" in value:
        import capo_codedeploy.types.timestamp

        out["end"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["end"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "start" in data:
        import capo_codedeploy.types.timestamp

        out["start"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["start"]
        )
    if "end" in data:
        import capo_codedeploy.types.timestamp

        out["end"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["end"]
        )
    return out
