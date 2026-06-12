"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetPreparedStatementOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.prepared_statement_details_list
    import aws_sdk_athena.types.unprocessed_prepared_statement_name_list


class BatchGetPreparedStatementOutput(TypedDict):
    prepared_statements: NotRequired[
        "aws_sdk_athena.types.prepared_statement_details_list.PreparedStatementDetailsList"
    ]
    """<p>The list of prepared statements returned.</p>"""
    unprocessed_prepared_statement_names: NotRequired[
        "aws_sdk_athena.types.unprocessed_prepared_statement_name_list.UnprocessedPreparedStatementNameList"
    ]
    """<p>A list of one or more prepared statements that were requested but could not be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetPreparedStatementOutput) -> dict:
    out: dict = {}
    if "prepared_statements" in value:
        import aws_sdk_athena.types.prepared_statement_details_list

        out["PreparedStatements"] = (
            aws_sdk_athena.types.prepared_statement_details_list.serialize_aws_json_1_1(
                value["prepared_statements"]
            )
        )
    if "unprocessed_prepared_statement_names" in value:
        import aws_sdk_athena.types.unprocessed_prepared_statement_name_list

        out["UnprocessedPreparedStatementNames"] = (
            aws_sdk_athena.types.unprocessed_prepared_statement_name_list.serialize_aws_json_1_1(
                value["unprocessed_prepared_statement_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetPreparedStatementOutput:
    out: BatchGetPreparedStatementOutput = {}  # type: ignore[typeddict-item]
    if "PreparedStatements" in data:
        import aws_sdk_athena.types.prepared_statement_details_list

        out["prepared_statements"] = (
            aws_sdk_athena.types.prepared_statement_details_list.deserialize_aws_json_1_1(
                data["PreparedStatements"]
            )
        )
    if "UnprocessedPreparedStatementNames" in data:
        import aws_sdk_athena.types.unprocessed_prepared_statement_name_list

        out["unprocessed_prepared_statement_names"] = (
            aws_sdk_athena.types.unprocessed_prepared_statement_name_list.deserialize_aws_json_1_1(
                data["UnprocessedPreparedStatementNames"]
            )
        )
    return out
