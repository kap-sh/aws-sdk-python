"""Generated from Smithy shape ``com.amazonaws.workmail#FolderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.folder_name
    import capo_workmail.types.retention_action
    import capo_workmail.types.retention_period


class FolderConfiguration(TypedDict, closed=True):
    name: "capo_workmail.types.folder_name.FolderName"
    """<p>The folder name.</p>"""
    action: "capo_workmail.types.retention_action.RetentionAction"
    """<p>The action to take on the folder contents at the end of the folder configuration period.</p>"""
    period: NotRequired["capo_workmail.types.retention_period.RetentionPeriod"]
    """<p>The number of days for which the folder-configuration action applies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FolderConfiguration) -> dict:
    out: dict = {}
    import capo_workmail.types.folder_name

    out["Name"] = capo_workmail.types.folder_name.serialize_aws_json_1_1(value["name"])
    import capo_workmail.types.retention_action

    out["Action"] = capo_workmail.types.retention_action.serialize_aws_json_1_1(
        value["action"]
    )
    if "period" in value:
        out["Period"] = value["period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FolderConfiguration:
    out: FolderConfiguration = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_workmail.types.folder_name

        out["name"] = capo_workmail.types.folder_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    else:
        raise DeserializationError("FolderConfiguration.name required")
    if "Action" in data:
        import capo_workmail.types.retention_action

        out["action"] = capo_workmail.types.retention_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("FolderConfiguration.action required")
    if "Period" in data:
        out["period"] = data["Period"]
    return out
