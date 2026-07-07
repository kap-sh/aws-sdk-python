"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.description_string
    import aws_sdk_bedrock_agent.types.include_exclude
    import aws_sdk_bedrock_agent.types.query_generation_columns
    import aws_sdk_bedrock_agent.types.query_generation_table_name


class QueryGenerationTable(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agent.types.query_generation_table_name.QueryGenerationTableName"
    """<p>The name of the table for which the other fields in this object apply.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.description_string.DescriptionString"
    ]
    """<p>A description of the table that helps the query engine understand the contents of the table.</p>"""
    inclusion: NotRequired["aws_sdk_bedrock_agent.types.include_exclude.IncludeExclude"]
    """<p>Specifies whether to include or exclude the table during query generation. If you specify <code>EXCLUDE</code>, the table will be ignored. If you specify <code>INCLUDE</code>, all other tables will be ignored.</p>"""
    columns: NotRequired[
        "aws_sdk_bedrock_agent.types.query_generation_columns.QueryGenerationColumns"
    ]
    """<p>An array of objects, each of which defines information about a column in the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationTable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "inclusion" in value:
        import aws_sdk_bedrock_agent.types.include_exclude

        out["inclusion"] = aws_sdk_bedrock_agent.types.include_exclude.serialize_json(
            value["inclusion"]
        )
    if "columns" in value:
        import aws_sdk_bedrock_agent.types.query_generation_columns

        out["columns"] = (
            aws_sdk_bedrock_agent.types.query_generation_columns.serialize_json(
                value["columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> QueryGenerationTable:
    out: QueryGenerationTable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("QueryGenerationTable.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "inclusion" in data:
        import aws_sdk_bedrock_agent.types.include_exclude

        out["inclusion"] = aws_sdk_bedrock_agent.types.include_exclude.deserialize_json(
            data["inclusion"]
        )
    if "columns" in data:
        import aws_sdk_bedrock_agent.types.query_generation_columns

        out["columns"] = (
            aws_sdk_bedrock_agent.types.query_generation_columns.deserialize_json(
                data["columns"]
            )
        )
    return out
