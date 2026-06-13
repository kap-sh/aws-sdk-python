"""Generated from Smithy shape ``com.amazonaws.redshiftdata#StatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.statement_data

StatementList: TypeAlias = list[
    "aws_sdk_redshift_data.types.statement_data.StatementData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementList) -> list:
    import aws_sdk_redshift_data.types.statement_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_data.types.statement_data.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StatementList:
    import aws_sdk_redshift_data.types.statement_data

    out: StatementList = []
    for item in data:
        out.append(
            aws_sdk_redshift_data.types.statement_data.deserialize_aws_json_1_1(item)
        )
    return out
