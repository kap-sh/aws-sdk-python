"""Generated from Smithy shape ``com.amazonaws.backup#BackupRulesInput``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_rule_input

BackupRulesInput: TypeAlias = list["aws_sdk_backup.types.backup_rule_input.BackupRuleInput"]


# --- restJson1 ser/de ---
def serialize_json(value: BackupRulesInput) -> list:
    import aws_sdk_backup.types.backup_rule_input
    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.backup_rule_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupRulesInput:
    import aws_sdk_backup.types.backup_rule_input
    out: BackupRulesInput = []
    for item in data:
        out.append(aws_sdk_backup.types.backup_rule_input.deserialize_json(item))
    return out