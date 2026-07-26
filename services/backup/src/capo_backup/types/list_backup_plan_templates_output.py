"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupPlanTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_plan_templates_list
    import capo_backup.types.string


class ListBackupPlanTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    backup_plan_templates_list: NotRequired[
        "capo_backup.types.backup_plan_templates_list.BackupPlanTemplatesList"
    ]
    """<p>An array of template list items containing metadata about your saved templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupPlanTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "backup_plan_templates_list" in value:
        import capo_backup.types.backup_plan_templates_list

        out["BackupPlanTemplatesList"] = (
            capo_backup.types.backup_plan_templates_list.serialize_json(
                value["backup_plan_templates_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBackupPlanTemplatesOutput:
    out: ListBackupPlanTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "BackupPlanTemplatesList" in data:
        import capo_backup.types.backup_plan_templates_list

        out["backup_plan_templates_list"] = (
            capo_backup.types.backup_plan_templates_list.deserialize_json(
                data["BackupPlanTemplatesList"]
            )
        )
    return out
