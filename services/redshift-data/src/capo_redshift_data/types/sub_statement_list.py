"""Generated from Smithy shape ``com.amazonaws.redshiftdata#SubStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_data.types.sub_statement_data

SubStatementList: TypeAlias = list[
    "capo_redshift_data.types.sub_statement_data.SubStatementData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubStatementList) -> list:
    import capo_redshift_data.types.sub_statement_data

    out: list = []
    for item in value:
        out.append(
            capo_redshift_data.types.sub_statement_data.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SubStatementList:
    import capo_redshift_data.types.sub_statement_data

    out: SubStatementList = []
    for item in data:
        out.append(
            capo_redshift_data.types.sub_statement_data.deserialize_aws_json_1_1(item)
        )
    return out
