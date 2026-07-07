"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.description_string
    import aws_sdk_bedrock_agent.types.include_exclude
    import aws_sdk_bedrock_agent.types.query_generation_column_name


class QueryGenerationColumn(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_bedrock_agent.types.query_generation_column_name.QueryGenerationColumnName"
    ]
    """<p>The name of the column for which the other fields in this object apply.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.description_string.DescriptionString"
    ]
    """<p>A description of the column that helps the query engine understand the contents of the column.</p>"""
    inclusion: NotRequired["aws_sdk_bedrock_agent.types.include_exclude.IncludeExclude"]
    """<p>Specifies whether to include or exclude the column during query generation. If you specify <code>EXCLUDE</code>, the column will be ignored. If you specify <code>INCLUDE</code>, all other columns in the table will be ignored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationColumn) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "inclusion" in value:
        import aws_sdk_bedrock_agent.types.include_exclude

        out["inclusion"] = aws_sdk_bedrock_agent.types.include_exclude.serialize_json(
            value["inclusion"]
        )
    return out


def deserialize_json(data: dict) -> QueryGenerationColumn:
    out: QueryGenerationColumn = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "inclusion" in data:
        import aws_sdk_bedrock_agent.types.include_exclude

        out["inclusion"] = aws_sdk_bedrock_agent.types.include_exclude.deserialize_json(
            data["inclusion"]
        )
    return out
