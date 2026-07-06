"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetQueryExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_execution_id_list


class BatchGetQueryExecutionInput(TypedDict, closed=True):
    query_execution_ids: (
        "aws_sdk_athena.types.query_execution_id_list.QueryExecutionIdList"
    )
    """<p>An array of query execution IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetQueryExecutionInput) -> dict:
    out: dict = {}
    import aws_sdk_athena.types.query_execution_id_list

    out["QueryExecutionIds"] = (
        aws_sdk_athena.types.query_execution_id_list.serialize_aws_json_1_1(
            value["query_execution_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetQueryExecutionInput:
    out: BatchGetQueryExecutionInput = {}  # type: ignore[typeddict-item]
    if "QueryExecutionIds" in data:
        import aws_sdk_athena.types.query_execution_id_list

        out["query_execution_ids"] = (
            aws_sdk_athena.types.query_execution_id_list.deserialize_aws_json_1_1(
                data["QueryExecutionIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetQueryExecutionInput.query_execution_ids required"
        )
    return out
