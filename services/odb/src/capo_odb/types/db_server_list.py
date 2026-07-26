"""Generated from Smithy shape ``com.amazonaws.odb#DbServerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.db_server_summary

DbServerList: TypeAlias = list["capo_odb.types.db_server_summary.DbServerSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbServerList) -> list:
    import capo_odb.types.db_server_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.db_server_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DbServerList:
    import capo_odb.types.db_server_summary

    out: DbServerList = []
    for item in data:
        out.append(capo_odb.types.db_server_summary.deserialize_aws_json_1_0(item))
    return out
