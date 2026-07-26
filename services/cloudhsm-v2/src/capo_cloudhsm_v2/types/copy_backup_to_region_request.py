"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CopyBackupToRegionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudhsm_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_id
    import capo_cloudhsm_v2.types.region
    import capo_cloudhsm_v2.types.tag_list


class CopyBackupToRegionRequest(TypedDict, closed=True):
    destination_region: "capo_cloudhsm_v2.types.region.Region"
    """<p>The AWS region that will contain your copied CloudHSM cluster backup.</p>"""
    backup_id: "capo_cloudhsm_v2.types.backup_id.BackupId"
    """<p>The ID of the backup that will be copied to the destination region. </p>"""
    tag_list: NotRequired["capo_cloudhsm_v2.types.tag_list.TagList"]
    """<p>Tags to apply to the destination backup during creation. If you specify tags, only these tags will be applied to the destination backup. If you do not specify tags, the service copies tags from the source backup to the destination backup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyBackupToRegionRequest) -> dict:
    out: dict = {}
    out["DestinationRegion"] = value["destination_region"]
    out["BackupId"] = value["backup_id"]
    if "tag_list" in value:
        import capo_cloudhsm_v2.types.tag_list

        out["TagList"] = capo_cloudhsm_v2.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyBackupToRegionRequest:
    out: CopyBackupToRegionRequest = {}  # type: ignore[typeddict-item]
    if "DestinationRegion" in data:
        out["destination_region"] = data["DestinationRegion"]
    else:
        raise DeserializationError(
            "CopyBackupToRegionRequest.destination_region required"
        )
    if "BackupId" in data:
        out["backup_id"] = data["BackupId"]
    else:
        raise DeserializationError("CopyBackupToRegionRequest.backup_id required")
    if "TagList" in data:
        import capo_cloudhsm_v2.types.tag_list

        out["tag_list"] = capo_cloudhsm_v2.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
