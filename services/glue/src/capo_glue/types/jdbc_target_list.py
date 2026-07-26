"""Generated from Smithy shape ``com.amazonaws.glue#JdbcTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.jdbc_target

JdbcTargetList: TypeAlias = list["capo_glue.types.jdbc_target.JdbcTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JdbcTargetList) -> list:
    import capo_glue.types.jdbc_target

    out: list = []
    for item in value:
        out.append(capo_glue.types.jdbc_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JdbcTargetList:
    import capo_glue.types.jdbc_target

    out: JdbcTargetList = []
    for item in data:
        out.append(capo_glue.types.jdbc_target.deserialize_aws_json_1_1(item))
    return out
