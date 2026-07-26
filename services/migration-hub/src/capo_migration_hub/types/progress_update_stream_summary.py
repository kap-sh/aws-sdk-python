"""Generated from Smithy shape ``com.amazonaws.migrationhub#ProgressUpdateStreamSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.progress_update_stream


class ProgressUpdateStreamSummary(TypedDict, closed=True):
    progress_update_stream_name: NotRequired[
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    ]
    """<p>The name of the ProgressUpdateStream. <i>Do not store personal data in this field.</i> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProgressUpdateStreamSummary) -> dict:
    out: dict = {}
    if "progress_update_stream_name" in value:
        out["ProgressUpdateStreamName"] = value["progress_update_stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProgressUpdateStreamSummary:
    out: ProgressUpdateStreamSummary = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStreamName" in data:
        out["progress_update_stream_name"] = data["ProgressUpdateStreamName"]
    return out
