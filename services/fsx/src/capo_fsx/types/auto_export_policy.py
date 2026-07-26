"""Generated from Smithy shape ``com.amazonaws.fsx#AutoExportPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.event_types


class AutoExportPolicy(TypedDict, closed=True):
    events: NotRequired["capo_fsx.types.event_types.EventTypes"]
    """<p>The <code>AutoExportPolicy</code> can have the following event values:</p> <ul> <li> <p> <code>NEW</code> - New files and directories are automatically exported to the data repository as they are added to the file system.</p> </li> <li> <p> <code>CHANGED</code> - Changes to files and directories on the file system are automatically exported to the data repository.</p> </li> <li> <p> <code>DELETED</code> - Files and directories are automatically deleted on the data repository when they are deleted on the file system.</p> </li> </ul> <p>You can define any combination of event types for your <code>AutoExportPolicy</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoExportPolicy) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_fsx.types.event_types

        out["Events"] = capo_fsx.types.event_types.serialize_aws_json_1_1(
            value["events"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoExportPolicy:
    out: AutoExportPolicy = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import capo_fsx.types.event_types

        out["events"] = capo_fsx.types.event_types.deserialize_aws_json_1_1(
            data["Events"]
        )
    return out
