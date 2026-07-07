"""Generated from Smithy shape ``com.amazonaws.quicksight#QueryExecutionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.query_execution_mode


class QueryExecutionOptions(TypedDict, closed=True):
    query_execution_mode: NotRequired[
        "aws_sdk_quicksight.types.query_execution_mode.QueryExecutionMode"
    ]
    """<p>A structure that describes the query execution mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryExecutionOptions) -> dict:
    out: dict = {}
    if "query_execution_mode" in value:
        import aws_sdk_quicksight.types.query_execution_mode

        out["QueryExecutionMode"] = (
            aws_sdk_quicksight.types.query_execution_mode.serialize_json(
                value["query_execution_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> QueryExecutionOptions:
    out: QueryExecutionOptions = {}  # type: ignore[typeddict-item]
    if "QueryExecutionMode" in data:
        import aws_sdk_quicksight.types.query_execution_mode

        out["query_execution_mode"] = (
            aws_sdk_quicksight.types.query_execution_mode.deserialize_json(
                data["QueryExecutionMode"]
            )
        )
    return out
