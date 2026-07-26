"""Generated from Smithy shape ``com.amazonaws.redshiftdata#SqlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_data.types.statement_string

SqlList: TypeAlias = list["capo_redshift_data.types.statement_string.StatementString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SqlList:
    return list(data)
