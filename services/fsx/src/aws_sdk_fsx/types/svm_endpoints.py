"""Generated from Smithy shape ``com.amazonaws.fsx#SvmEndpoints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.svm_endpoint


class SvmEndpoints(TypedDict, closed=True):
    iscsi: NotRequired["aws_sdk_fsx.types.svm_endpoint.SvmEndpoint"]
    """<p>An endpoint for connecting using the Internet Small Computer Systems Interface (iSCSI) protocol.</p>"""
    management: NotRequired["aws_sdk_fsx.types.svm_endpoint.SvmEndpoint"]
    """<p>An endpoint for managing SVMs using the NetApp ONTAP CLI, NetApp ONTAP API, or NetApp CloudManager.</p>"""
    nfs: NotRequired["aws_sdk_fsx.types.svm_endpoint.SvmEndpoint"]
    """<p>An endpoint for connecting using the Network File System (NFS) protocol.</p>"""
    smb: NotRequired["aws_sdk_fsx.types.svm_endpoint.SvmEndpoint"]
    """<p>An endpoint for connecting using the Server Message Block (SMB) protocol.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SvmEndpoints) -> dict:
    out: dict = {}
    if "iscsi" in value:
        import aws_sdk_fsx.types.svm_endpoint

        out["Iscsi"] = aws_sdk_fsx.types.svm_endpoint.serialize_aws_json_1_1(
            value["iscsi"]
        )
    if "management" in value:
        import aws_sdk_fsx.types.svm_endpoint

        out["Management"] = aws_sdk_fsx.types.svm_endpoint.serialize_aws_json_1_1(
            value["management"]
        )
    if "nfs" in value:
        import aws_sdk_fsx.types.svm_endpoint

        out["Nfs"] = aws_sdk_fsx.types.svm_endpoint.serialize_aws_json_1_1(value["nfs"])
    if "smb" in value:
        import aws_sdk_fsx.types.svm_endpoint

        out["Smb"] = aws_sdk_fsx.types.svm_endpoint.serialize_aws_json_1_1(value["smb"])
    return out


def deserialize_aws_json_1_1(data: dict) -> SvmEndpoints:
    out: SvmEndpoints = {}  # type: ignore[typeddict-item]
    if "Iscsi" in data:
        import aws_sdk_fsx.types.svm_endpoint

        out["iscsi"] = aws_sdk_fsx.types.svm_endpoint.deserialize_aws_json_1_1(
            data["Iscsi"]
        )
    if "Management" in data:
        import aws_sdk_fsx.types.svm_endpoint

        out["management"] = aws_sdk_fsx.types.svm_endpoint.deserialize_aws_json_1_1(
            data["Management"]
        )
    if "Nfs" in data:
        import aws_sdk_fsx.types.svm_endpoint

        out["nfs"] = aws_sdk_fsx.types.svm_endpoint.deserialize_aws_json_1_1(
            data["Nfs"]
        )
    if "Smb" in data:
        import aws_sdk_fsx.types.svm_endpoint

        out["smb"] = aws_sdk_fsx.types.svm_endpoint.deserialize_aws_json_1_1(
            data["Smb"]
        )
    return out
