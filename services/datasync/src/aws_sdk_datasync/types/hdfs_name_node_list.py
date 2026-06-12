"""Generated from Smithy shape ``com.amazonaws.datasync#HdfsNameNodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.hdfs_name_node

HdfsNameNodeList: TypeAlias = list["aws_sdk_datasync.types.hdfs_name_node.HdfsNameNode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HdfsNameNodeList) -> list:
    import aws_sdk_datasync.types.hdfs_name_node

    out: list = []
    for item in value:
        out.append(aws_sdk_datasync.types.hdfs_name_node.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HdfsNameNodeList:
    import aws_sdk_datasync.types.hdfs_name_node

    out: HdfsNameNodeList = []
    for item in data:
        out.append(aws_sdk_datasync.types.hdfs_name_node.deserialize_aws_json_1_1(item))
    return out
