"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.description_string
    import capo_bedrock_agent.types.include_exclude
    import capo_bedrock_agent.types.query_generation_column_name


class QueryGenerationColumn(TypedDict, closed=True):
    name: NotRequired[
        "capo_bedrock_agent.types.query_generation_column_name.QueryGenerationColumnName"
    ]
    """<p>The name of the column for which the other fields in this object apply.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.description_string.DescriptionString"
    ]
    """<p>A description of the column that helps the query engine understand the contents of the column.</p>"""
    inclusion: NotRequired["capo_bedrock_agent.types.include_exclude.IncludeExclude"]
    """<p>Specifies whether to include or exclude the column during query generation. If you specify <code>EXCLUDE</code>, the column will be ignored. If you specify <code>INCLUDE</code>, all other columns in the table will be ignored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationColumn) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "inclusion" in value:
        import capo_bedrock_agent.types.include_exclude

        out["inclusion"] = capo_bedrock_agent.types.include_exclude.serialize_json(
            value["inclusion"]
        )
    return out


def deserialize_json(data: dict) -> QueryGenerationColumn:
    out: QueryGenerationColumn = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("inclusion") is not None:
        import capo_bedrock_agent.types.include_exclude

        out["inclusion"] = capo_bedrock_agent.types.include_exclude.deserialize_json(
            data["inclusion"]
        )
    return out
