"""Generated from Smithy shape ``com.amazonaws.athena#ListQueryExecutionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_execution_id_list
    import aws_sdk_athena.types.token


class ListQueryExecutionsOutput(TypedDict):
    query_execution_ids: NotRequired[
        "aws_sdk_athena.types.query_execution_id_list.QueryExecutionIdList"
    ]
    """<p>The unique IDs of each query execution as an array of strings.</p>"""
    next_token: NotRequired["aws_sdk_athena.types.token.Token"]
    """<p>A token to be used by the next request if this request is truncated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQueryExecutionsOutput) -> dict:
    out: dict = {}
    if "query_execution_ids" in value:
        import aws_sdk_athena.types.query_execution_id_list

        out["QueryExecutionIds"] = (
            aws_sdk_athena.types.query_execution_id_list.serialize_aws_json_1_1(
                value["query_execution_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQueryExecutionsOutput:
    out: ListQueryExecutionsOutput = {}  # type: ignore[typeddict-item]
    if "QueryExecutionIds" in data:
        import aws_sdk_athena.types.query_execution_id_list

        out["query_execution_ids"] = (
            aws_sdk_athena.types.query_execution_id_list.deserialize_aws_json_1_1(
                data["QueryExecutionIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
