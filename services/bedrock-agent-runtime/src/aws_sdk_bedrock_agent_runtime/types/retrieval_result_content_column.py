"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultContentColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column_type


class RetrievalResultContentColumn(TypedDict, closed=True):
    column_name: NotRequired["str"]
    """<p>The name of the column.</p>"""
    column_value: NotRequired["str"]
    """<p>The value in the column.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column_type.RetrievalResultContentColumnType"
    ]
    """<p>The data type of the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultContentColumn) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["columnName"] = value["column_name"]
    if "column_value" in value:
        out["columnValue"] = value["column_value"]
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrievalResultContentColumn:
    out: RetrievalResultContentColumn = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    if "columnValue" in data:
        out["column_value"] = data["columnValue"]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column_type.deserialize_json(
                data["type"]
            )
        )
    return out
