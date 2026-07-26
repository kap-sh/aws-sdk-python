"""Generated from Smithy shape ``com.amazonaws.glue#StatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.statement

StatementList: TypeAlias = list["capo_glue.types.statement.Statement"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementList) -> list:
    import capo_glue.types.statement

    out: list = []
    for item in value:
        out.append(capo_glue.types.statement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StatementList:
    import capo_glue.types.statement

    out: StatementList = []
    for item in data:
        out.append(capo_glue.types.statement.deserialize_aws_json_1_1(item))
    return out
