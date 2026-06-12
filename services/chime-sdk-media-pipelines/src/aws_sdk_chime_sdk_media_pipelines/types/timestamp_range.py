"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#TimestampRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.timestamp


class TimestampRange(TypedDict):
    start_timestamp: "aws_sdk_chime_sdk_media_pipelines.types.timestamp.Timestamp"
    """<p>The starting timestamp for the specified range.</p>"""
    end_timestamp: "aws_sdk_chime_sdk_media_pipelines.types.timestamp.Timestamp"
    """<p>The ending timestamp for the specified range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestampRange) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.timestamp

    out["StartTimestamp"] = (
        aws_sdk_chime_sdk_media_pipelines.types.timestamp.serialize_json(
            value["start_timestamp"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.timestamp

    out["EndTimestamp"] = (
        aws_sdk_chime_sdk_media_pipelines.types.timestamp.serialize_json(
            value["end_timestamp"]
        )
    )
    return out


def deserialize_json(data: dict) -> TimestampRange:
    out: TimestampRange = {}  # type: ignore[typeddict-item]
    if "StartTimestamp" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.timestamp

        out["start_timestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    else:
        raise DeserializationError("TimestampRange.start_timestamp required")
    if "EndTimestamp" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.timestamp

        out["end_timestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    else:
        raise DeserializationError("TimestampRange.end_timestamp required")
    return out
