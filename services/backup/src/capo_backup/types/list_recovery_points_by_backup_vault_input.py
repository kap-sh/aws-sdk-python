"""Generated from Smithy shape ``com.amazonaws.backup#ListRecoveryPointsByBackupVaultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.max_results
    import capo_backup.types.resource_type
    import capo_backup.types.string
    import capo_backup.types.timestamp


class ListRecoveryPointsByBackupVaultInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p> <note> <p>Backup vault name might not be available when a supported service creates the backup.</p> </note>"""
    backup_vault_account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>This parameter will sort the list of recovery points by account ID.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p>"""
    by_resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>Returns only recovery points that match the specified resource Amazon Resource Name (ARN).</p>"""
    by_resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>Returns only recovery points that match the specified resource type(s):</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>"""
    by_backup_plan_id: NotRequired["capo_backup.types.string.string"]
    """<p>Returns only recovery points that match the specified backup plan ID.</p>"""
    by_created_before: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only recovery points that were created before the specified timestamp.</p>"""
    by_created_after: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Returns only recovery points that were created after the specified timestamp.</p>"""
    by_parent_recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>This returns only recovery points that match the specified parent (composite) recovery point Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPointsByBackupVaultInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecoveryPointsByBackupVaultInput:
    out: ListRecoveryPointsByBackupVaultInput = {}  # type: ignore[typeddict-item]
    return out
