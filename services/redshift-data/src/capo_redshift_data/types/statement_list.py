"""Generated from Smithy shape ``com.amazonaws.redshiftdata#StatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_data.types.statement_data

StatementList: TypeAlias = list["capo_redshift_data.types.statement_data.StatementData"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementList) -> list:
    import capo_redshift_data.types.statement_data

    out: list = []
    for item in value:
        out.append(capo_redshift_data.types.statement_data.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StatementList:
    import capo_redshift_data.types.statement_data

    out: StatementList = []
    for item in data:
        out.append(
            capo_redshift_data.types.statement_data.deserialize_aws_json_1_1(item)
        )
    return out
