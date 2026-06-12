"""Generated from Smithy shape ``com.amazonaws.athena#PreparedStatementDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.prepared_statement

PreparedStatementDetailsList: TypeAlias = list[
    "aws_sdk_athena.types.prepared_statement.PreparedStatement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreparedStatementDetailsList) -> list:
    import aws_sdk_athena.types.prepared_statement

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.prepared_statement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PreparedStatementDetailsList:
    import aws_sdk_athena.types.prepared_statement

    out: PreparedStatementDetailsList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.prepared_statement.deserialize_aws_json_1_1(item)
        )
    return out
