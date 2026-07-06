"""Generated from Smithy shape ``com.amazonaws.efs#DeleteReplicationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.deletion_mode
    import aws_sdk_efs.types.file_system_id


class DeleteReplicationConfigurationRequest(TypedDict, closed=True):
    source_file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the source file system in the replication configuration.</p>"""
    deletion_mode: NotRequired["aws_sdk_efs.types.deletion_mode.DeletionMode"]
    """<p>When replicating across Amazon Web Services accounts or across Amazon Web Services Regions, Amazon EFS deletes the replication configuration from both the source and destination account or Region (<code>ALL_CONFIGURATIONS</code>) by default. If there's a configuration or permissions issue that prevents Amazon EFS from deleting the replication configuration from both sides, you can use the <code>LOCAL_CONFIGURATION_ONLY</code> mode to delete the replication configuration from only the local side (the account or Region from which the delete is performed). </p> <note> <p>Only use the <code>LOCAL_CONFIGURATION_ONLY</code> mode in the case that Amazon EFS is unable to delete the replication configuration in both the source and destination account or Region. Deleting the local configuration leaves the configuration in the other account or Region unrecoverable.</p> <p>Additionally, do not use this mode for same-account, same-region replication as doing so results in a BadRequest exception error.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReplicationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReplicationConfigurationRequest:
    out: DeleteReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
