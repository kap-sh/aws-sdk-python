"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.curated_queries
    import capo_bedrock_agent.types.query_generation_tables


class QueryGenerationContext(TypedDict, closed=True):
    tables: NotRequired[
        "capo_bedrock_agent.types.query_generation_tables.QueryGenerationTables"
    ]
    """<p>An array of objects, each of which defines information about a table in the database.</p>"""
    curated_queries: NotRequired[
        "capo_bedrock_agent.types.curated_queries.CuratedQueries"
    ]
    """<p>An array of objects, each of which defines information about example queries to help the query engine generate appropriate SQL queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationContext) -> dict:
    out: dict = {}
    if "tables" in value:
        import capo_bedrock_agent.types.query_generation_tables

        out["tables"] = capo_bedrock_agent.types.query_generation_tables.serialize_json(
            value["tables"]
        )
    if "curated_queries" in value:
        import capo_bedrock_agent.types.curated_queries

        out["curatedQueries"] = capo_bedrock_agent.types.curated_queries.serialize_json(
            value["curated_queries"]
        )
    return out


def deserialize_json(data: dict) -> QueryGenerationContext:
    out: QueryGenerationContext = {}  # type: ignore[typeddict-item]
    if "tables" in data:
        import capo_bedrock_agent.types.query_generation_tables

        out["tables"] = (
            capo_bedrock_agent.types.query_generation_tables.deserialize_json(
                data["tables"]
            )
        )
    if "curatedQueries" in data:
        import capo_bedrock_agent.types.curated_queries

        out["curated_queries"] = (
            capo_bedrock_agent.types.curated_queries.deserialize_json(
                data["curatedQueries"]
            )
        )
    return out
