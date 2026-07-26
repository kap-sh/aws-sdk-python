"""Generated from Smithy shape ``com.amazonaws.athena#PreparedStatementNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.statement_name

PreparedStatementNameList: TypeAlias = list[
    "capo_athena.types.statement_name.StatementName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreparedStatementNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PreparedStatementNameList:
    return list(data)
