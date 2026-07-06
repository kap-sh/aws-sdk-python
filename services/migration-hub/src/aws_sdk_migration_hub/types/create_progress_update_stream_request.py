"""Generated from Smithy shape ``com.amazonaws.migrationhub#CreateProgressUpdateStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.dry_run
    import aws_sdk_migration_hub.types.progress_update_stream


class CreateProgressUpdateStreamRequest(TypedDict, closed=True):
    progress_update_stream_name: (
        "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream. <i>Do not store personal data in this field.</i> </p>"""
    dry_run: "aws_sdk_migration_hub.types.dry_run.DryRun"
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProgressUpdateStreamRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStreamName"] = value["progress_update_stream_name"]
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProgressUpdateStreamRequest:
    out: CreateProgressUpdateStreamRequest = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStreamName" in data:
        out["progress_update_stream_name"] = data["ProgressUpdateStreamName"]
    else:
        raise DeserializationError(
            "CreateProgressUpdateStreamRequest.progress_update_stream_name required"
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
