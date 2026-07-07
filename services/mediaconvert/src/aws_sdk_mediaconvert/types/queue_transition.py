"""Generated from Smithy shape ``com.amazonaws.mediaconvert#QueueTransition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__timestamp_unix


class QueueTransition(TypedDict, closed=True):
    destination_queue: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The queue that the job was on after the transition."""
    source_queue: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The queue that the job was on before the transition."""
    timestamp: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The time, in Unix epoch format, that the job moved from the source queue to the destination queue."""


# --- restJson1 ser/de ---
def serialize_json(value: QueueTransition) -> dict:
    out: dict = {}
    if "destination_queue" in value:
        out["destinationQueue"] = value["destination_queue"]
    if "source_queue" in value:
        out["sourceQueue"] = value["source_queue"]
    if "timestamp" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["timestamp"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> QueueTransition:
    out: QueueTransition = {}  # type: ignore[typeddict-item]
    if "destinationQueue" in data:
        out["destination_queue"] = data["destinationQueue"]
    if "sourceQueue" in data:
        out["source_queue"] = data["sourceQueue"]
    if "timestamp" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["timestamp"] = aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
            data["timestamp"]
        )
    return out
