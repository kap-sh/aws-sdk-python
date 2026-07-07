"""Generated from Smithy shape ``com.amazonaws.fsx#AutoImportPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.event_types


class AutoImportPolicy(TypedDict, closed=True):
    events: NotRequired["aws_sdk_fsx.types.event_types.EventTypes"]
    """<p>The <code>AutoImportPolicy</code> can have the following event values:</p> <ul> <li> <p> <code>NEW</code> - Amazon FSx automatically imports metadata of files added to the linked S3 bucket that do not currently exist in the FSx file system.</p> </li> <li> <p> <code>CHANGED</code> - Amazon FSx automatically updates file metadata and invalidates existing file content on the file system as files change in the data repository.</p> </li> <li> <p> <code>DELETED</code> - Amazon FSx automatically deletes files on the file system as corresponding files are deleted in the data repository.</p> </li> </ul> <p>You can define any combination of event types for your <code>AutoImportPolicy</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoImportPolicy) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_fsx.types.event_types

        out["Events"] = aws_sdk_fsx.types.event_types.serialize_aws_json_1_1(
            value["events"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoImportPolicy:
    out: AutoImportPolicy = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_fsx.types.event_types

        out["events"] = aws_sdk_fsx.types.event_types.deserialize_aws_json_1_1(
            data["Events"]
        )
    return out
