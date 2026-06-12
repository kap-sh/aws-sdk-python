"""Generated from Smithy shape ``com.amazonaws.datasync#QopConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.hdfs_data_transfer_protection
    import aws_sdk_datasync.types.hdfs_rpc_protection


class QopConfiguration(TypedDict):
    rpc_protection: NotRequired[
        "aws_sdk_datasync.types.hdfs_rpc_protection.HdfsRpcProtection"
    ]
    """<p>The RPC protection setting configured on the HDFS cluster. This setting corresponds to your <code>hadoop.rpc.protection</code> setting in your <code>core-site.xml</code> file on your Hadoop cluster.</p>"""
    data_transfer_protection: NotRequired[
        "aws_sdk_datasync.types.hdfs_data_transfer_protection.HdfsDataTransferProtection"
    ]
    """<p>The data transfer protection setting configured on the HDFS cluster. This setting corresponds to your <code>dfs.data.transfer.protection</code> setting in the <code>hdfs-site.xml</code> file on your Hadoop cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QopConfiguration) -> dict:
    out: dict = {}
    if "rpc_protection" in value:
        import aws_sdk_datasync.types.hdfs_rpc_protection

        out["RpcProtection"] = (
            aws_sdk_datasync.types.hdfs_rpc_protection.serialize_aws_json_1_1(
                value["rpc_protection"]
            )
        )
    if "data_transfer_protection" in value:
        import aws_sdk_datasync.types.hdfs_data_transfer_protection

        out["DataTransferProtection"] = (
            aws_sdk_datasync.types.hdfs_data_transfer_protection.serialize_aws_json_1_1(
                value["data_transfer_protection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QopConfiguration:
    out: QopConfiguration = {}  # type: ignore[typeddict-item]
    if "RpcProtection" in data:
        import aws_sdk_datasync.types.hdfs_rpc_protection

        out["rpc_protection"] = (
            aws_sdk_datasync.types.hdfs_rpc_protection.deserialize_aws_json_1_1(
                data["RpcProtection"]
            )
        )
    if "DataTransferProtection" in data:
        import aws_sdk_datasync.types.hdfs_data_transfer_protection

        out["data_transfer_protection"] = (
            aws_sdk_datasync.types.hdfs_data_transfer_protection.deserialize_aws_json_1_1(
                data["DataTransferProtection"]
            )
        )
    return out
