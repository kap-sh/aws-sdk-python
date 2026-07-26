"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreTestingInferredMetadataInput``."""

from typing_extensions import NotRequired, TypedDict


class GetRestoreTestingInferredMetadataInput(TypedDict, closed=True):
    backup_vault_account_id: NotRequired["str"]
    """<p>The account ID of the specified backup vault.</p>"""
    backup_vault_name: "str"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web ServicesRegion where they are created. They consist of letters, numbers, and hyphens.</p>"""
    recovery_point_arn: "str"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreTestingInferredMetadataInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRestoreTestingInferredMetadataInput:
    out: GetRestoreTestingInferredMetadataInput = {}  # type: ignore[typeddict-item]
    return out
