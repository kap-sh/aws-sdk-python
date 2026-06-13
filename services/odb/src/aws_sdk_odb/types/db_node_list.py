"""Generated from Smithy shape ``com.amazonaws.odb#DbNodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_node_summary

DbNodeList: TypeAlias = list["aws_sdk_odb.types.db_node_summary.DbNodeSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbNodeList) -> list:
    import aws_sdk_odb.types.db_node_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_odb.types.db_node_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DbNodeList:
    import aws_sdk_odb.types.db_node_summary

    out: DbNodeList = []
    for item in data:
        out.append(aws_sdk_odb.types.db_node_summary.deserialize_aws_json_1_0(item))
    return out
