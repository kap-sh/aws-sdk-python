"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetPreparedStatementOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.prepared_statement_details_list
    import capo_athena.types.unprocessed_prepared_statement_name_list


class BatchGetPreparedStatementOutput(TypedDict, closed=True):
    prepared_statements: NotRequired[
        "capo_athena.types.prepared_statement_details_list.PreparedStatementDetailsList"
    ]
    """<p>The list of prepared statements returned.</p>"""
    unprocessed_prepared_statement_names: NotRequired[
        "capo_athena.types.unprocessed_prepared_statement_name_list.UnprocessedPreparedStatementNameList"
    ]
    """<p>A list of one or more prepared statements that were requested but could not be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetPreparedStatementOutput) -> dict:
    out: dict = {}
    if "prepared_statements" in value:
        import capo_athena.types.prepared_statement_details_list

        out["PreparedStatements"] = (
            capo_athena.types.prepared_statement_details_list.serialize_aws_json_1_1(
                value["prepared_statements"]
            )
        )
    if "unprocessed_prepared_statement_names" in value:
        import capo_athena.types.unprocessed_prepared_statement_name_list

        out["UnprocessedPreparedStatementNames"] = (
            capo_athena.types.unprocessed_prepared_statement_name_list.serialize_aws_json_1_1(
                value["unprocessed_prepared_statement_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetPreparedStatementOutput:
    out: BatchGetPreparedStatementOutput = {}  # type: ignore[typeddict-item]
    if "PreparedStatements" in data:
        import capo_athena.types.prepared_statement_details_list

        out["prepared_statements"] = (
            capo_athena.types.prepared_statement_details_list.deserialize_aws_json_1_1(
                data["PreparedStatements"]
            )
        )
    if "UnprocessedPreparedStatementNames" in data:
        import capo_athena.types.unprocessed_prepared_statement_name_list

        out["unprocessed_prepared_statement_names"] = (
            capo_athena.types.unprocessed_prepared_statement_name_list.deserialize_aws_json_1_1(
                data["UnprocessedPreparedStatementNames"]
            )
        )
    return out
