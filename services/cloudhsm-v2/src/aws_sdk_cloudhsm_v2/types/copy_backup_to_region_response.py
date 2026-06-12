"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CopyBackupToRegionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.destination_backup


class CopyBackupToRegionResponse(TypedDict):
    destination_backup: NotRequired[
        "aws_sdk_cloudhsm_v2.types.destination_backup.DestinationBackup"
    ]
    """<p>Information on the backup that will be copied to the destination region, including CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the destination backup will be the same as that of the source backup.</p> <p>You will need to use the <code>sourceBackupID</code> returned in this operation to use the <a>DescribeBackups</a> operation on the backup that will be copied to the destination region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyBackupToRegionResponse) -> dict:
    out: dict = {}
    if "destination_backup" in value:
        import aws_sdk_cloudhsm_v2.types.destination_backup

        out["DestinationBackup"] = (
            aws_sdk_cloudhsm_v2.types.destination_backup.serialize_aws_json_1_1(
                value["destination_backup"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyBackupToRegionResponse:
    out: CopyBackupToRegionResponse = {}  # type: ignore[typeddict-item]
    if "DestinationBackup" in data:
        import aws_sdk_cloudhsm_v2.types.destination_backup

        out["destination_backup"] = (
            aws_sdk_cloudhsm_v2.types.destination_backup.deserialize_aws_json_1_1(
                data["DestinationBackup"]
            )
        )
    return out
