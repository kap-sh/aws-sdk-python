"""Generated from Smithy shape ``com.amazonaws.datasync#FsxUpdateProtocol``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.fsx_protocol_nfs
    import capo_datasync.types.fsx_update_protocol_smb


class FsxUpdateProtocol(TypedDict, closed=True):
    nfs: NotRequired["capo_datasync.types.fsx_protocol_nfs.FsxProtocolNfs"]
    smb: NotRequired["capo_datasync.types.fsx_update_protocol_smb.FsxUpdateProtocolSmb"]
    """<p>Specifies the Server Message Block (SMB) protocol configuration that DataSync uses to access your FSx for ONTAP file system's storage virtual machine (SVM).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FsxUpdateProtocol) -> dict:
    out: dict = {}
    if "nfs" in value:
        import capo_datasync.types.fsx_protocol_nfs

        out["NFS"] = capo_datasync.types.fsx_protocol_nfs.serialize_aws_json_1_1(
            value["nfs"]
        )
    if "smb" in value:
        import capo_datasync.types.fsx_update_protocol_smb

        out["SMB"] = capo_datasync.types.fsx_update_protocol_smb.serialize_aws_json_1_1(
            value["smb"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FsxUpdateProtocol:
    out: FsxUpdateProtocol = {}  # type: ignore[typeddict-item]
    if "NFS" in data:
        import capo_datasync.types.fsx_protocol_nfs

        out["nfs"] = capo_datasync.types.fsx_protocol_nfs.deserialize_aws_json_1_1(
            data["NFS"]
        )
    if "SMB" in data:
        import capo_datasync.types.fsx_update_protocol_smb

        out["smb"] = (
            capo_datasync.types.fsx_update_protocol_smb.deserialize_aws_json_1_1(
                data["SMB"]
            )
        )
    return out
