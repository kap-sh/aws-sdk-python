"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobCreator``."""

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError


class ScanJobCreator(TypedDict, closed=True):
    backup_plan_arn: "str"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, <code>arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50</code>.</p>"""
    backup_plan_id: "str"
    """<p>The ID of the backup plan.</p>"""
    backup_plan_version: "str"
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.</p>"""
    backup_rule_id: "str"
    """<p>Uniquely identifies the backup rule that initiated the scan job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanJobCreator) -> dict:
    out: dict = {}
    out["BackupPlanArn"] = value["backup_plan_arn"]
    out["BackupPlanId"] = value["backup_plan_id"]
    out["BackupPlanVersion"] = value["backup_plan_version"]
    out["BackupRuleId"] = value["backup_rule_id"]
    return out


def deserialize_json(data: dict) -> ScanJobCreator:
    out: ScanJobCreator = {}  # type: ignore[typeddict-item]
    if "BackupPlanArn" in data:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    else:
        raise DeserializationError("ScanJobCreator.backup_plan_arn required")
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    else:
        raise DeserializationError("ScanJobCreator.backup_plan_id required")
    if "BackupPlanVersion" in data:
        out["backup_plan_version"] = data["BackupPlanVersion"]
    else:
        raise DeserializationError("ScanJobCreator.backup_plan_version required")
    if "BackupRuleId" in data:
        out["backup_rule_id"] = data["BackupRuleId"]
    else:
        raise DeserializationError("ScanJobCreator.backup_rule_id required")
    return out
