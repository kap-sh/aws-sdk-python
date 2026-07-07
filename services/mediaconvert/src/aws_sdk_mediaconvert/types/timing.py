"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Timing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__timestamp_unix


class Timing(TypedDict, closed=True):
    finish_time: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The time, in Unix epoch format, that the transcoding job finished"""
    start_time: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The time, in Unix epoch format, that transcoding for the job began."""
    submit_time: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The time, in Unix epoch format, that you submitted the job."""


# --- restJson1 ser/de ---
def serialize_json(value: Timing) -> dict:
    out: dict = {}
    if "finish_time" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["finishTime"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["finish_time"]
        )
    if "start_time" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["startTime"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["start_time"]
        )
    if "submit_time" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["submitTime"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["submit_time"]
        )
    return out


def deserialize_json(data: dict) -> Timing:
    out: Timing = {}  # type: ignore[typeddict-item]
    if "finishTime" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["finish_time"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["finishTime"]
            )
        )
    if "startTime" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["start_time"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["startTime"]
            )
        )
    if "submitTime" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["submit_time"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["submitTime"]
            )
        )
    return out
