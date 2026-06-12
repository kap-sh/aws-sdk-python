"""Generated from Smithy shape ``com.amazonaws.athena#PreparedStatementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.prepared_statement_summary

PreparedStatementsList: TypeAlias = list[
    "aws_sdk_athena.types.prepared_statement_summary.PreparedStatementSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreparedStatementsList) -> list:
    import aws_sdk_athena.types.prepared_statement_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_athena.types.prepared_statement_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PreparedStatementsList:
    import aws_sdk_athena.types.prepared_statement_summary

    out: PreparedStatementsList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.prepared_statement_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
