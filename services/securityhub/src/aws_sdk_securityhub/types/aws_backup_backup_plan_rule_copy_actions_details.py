"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanRuleCopyActionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_lifecycle_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsBackupBackupPlanRuleCopyActionsDetails(TypedDict):
    destination_backup_vault_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. </p>"""
    lifecycle: NotRequired[
        "aws_sdk_securityhub.types.aws_backup_backup_plan_lifecycle_details.AwsBackupBackupPlanLifecycleDetails"
    ]
    """<p>Defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define. If you don't specify a lifecycle, Backup applies the lifecycle policy of the source backup to the destination backup.</p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanRuleCopyActionsDetails) -> dict:
    out: dict = {}
    if "destination_backup_vault_arn" in value:
        out["DestinationBackupVaultArn"] = value["destination_backup_vault_arn"]
    if "lifecycle" in value:
        import aws_sdk_securityhub.types.aws_backup_backup_plan_lifecycle_details

        out["Lifecycle"] = (
            aws_sdk_securityhub.types.aws_backup_backup_plan_lifecycle_details.serialize_json(
                value["lifecycle"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsBackupBackupPlanRuleCopyActionsDetails:
    out: AwsBackupBackupPlanRuleCopyActionsDetails = {}  # type: ignore[typeddict-item]
    if "DestinationBackupVaultArn" in data:
        out["destination_backup_vault_arn"] = data["DestinationBackupVaultArn"]
    if "Lifecycle" in data:
        import aws_sdk_securityhub.types.aws_backup_backup_plan_lifecycle_details

        out["lifecycle"] = (
            aws_sdk_securityhub.types.aws_backup_backup_plan_lifecycle_details.deserialize_json(
                data["Lifecycle"]
            )
        )
    return out
