"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionFilesListedDetail``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.long


class TaskExecutionFilesListedDetail(TypedDict):
    at_source: "aws_sdk_datasync.types.long.long"
    """<p>The number of files or objects that DataSync finds at your source location.</p> <ul> <li> <p>With a <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html\">manifest</a>, DataSync lists only what's in your manifest (and not everything at your source location).</p> </li> <li> <p>With an include <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html\">filter</a>, DataSync lists only what matches the filter at your source location.</p> </li> <li> <p>With an exclude filter, DataSync lists everything at your source location before applying the filter.</p> </li> </ul>"""
    at_destination_for_delete: "aws_sdk_datasync.types.long.long"
    """<p>The number of files or objects that DataSync finds at your destination location. This counter is only applicable if you <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-file-object-handling\">configure your task</a> to delete data in the destination that isn't in the source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionFilesListedDetail) -> dict:
    out: dict = {}
    out["AtSource"] = value.get("at_source", 0)
    out["AtDestinationForDelete"] = value.get("at_destination_for_delete", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskExecutionFilesListedDetail:
    out: TaskExecutionFilesListedDetail = {}  # type: ignore[typeddict-item]
    if "AtSource" in data:
        out["at_source"] = data["AtSource"]
    else:
        out["at_source"] = 0
    if "AtDestinationForDelete" in data:
        out["at_destination_for_delete"] = data["AtDestinationForDelete"]
    else:
        out["at_destination_for_delete"] = 0
    return out
