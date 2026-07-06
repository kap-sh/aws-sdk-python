"""Generated from Smithy shape ``com.amazonaws.devopsguru#EndTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.timestamp


class EndTimeRange(TypedDict, closed=True):
    from_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The earliest end time in the time range. </p>"""
    to_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The latest end time in the time range. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndTimeRange) -> dict:
    out: dict = {}
    if "from_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["FromTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["from_time"]
        )
    if "to_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["ToTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["to_time"]
        )
    return out


def deserialize_json(data: dict) -> EndTimeRange:
    out: EndTimeRange = {}  # type: ignore[typeddict-item]
    if "FromTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["from_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["FromTime"]
        )
    if "ToTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["to_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["ToTime"]
        )
    return out
