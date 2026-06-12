"""Generated from Smithy shape ``com.amazonaws.athena#UnprocessedPreparedStatementNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.unprocessed_prepared_statement_name

UnprocessedPreparedStatementNameList: TypeAlias = list[
    "aws_sdk_athena.types.unprocessed_prepared_statement_name.UnprocessedPreparedStatementName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedPreparedStatementNameList) -> list:
    import aws_sdk_athena.types.unprocessed_prepared_statement_name

    out: list = []
    for item in value:
        out.append(
            aws_sdk_athena.types.unprocessed_prepared_statement_name.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnprocessedPreparedStatementNameList:
    import aws_sdk_athena.types.unprocessed_prepared_statement_name

    out: UnprocessedPreparedStatementNameList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.unprocessed_prepared_statement_name.deserialize_aws_json_1_1(
                item
            )
        )
    return out
