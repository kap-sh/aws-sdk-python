"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CuratedQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.natural_language_string
    import capo_bedrock_agent.types.sql_string


class CuratedQuery(TypedDict, closed=True):
    natural_language: (
        "capo_bedrock_agent.types.natural_language_string.NaturalLanguageString"
    )
    """<p>An example natural language query.</p>"""
    sql: "capo_bedrock_agent.types.sql_string.SqlString"
    """<p>The SQL equivalent of the natural language query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CuratedQuery) -> dict:
    out: dict = {}
    out["naturalLanguage"] = value["natural_language"]
    out["sql"] = value["sql"]
    return out


def deserialize_json(data: dict) -> CuratedQuery:
    out: CuratedQuery = {}  # type: ignore[typeddict-item]
    if "naturalLanguage" in data:
        out["natural_language"] = data["naturalLanguage"]
    else:
        raise DeserializationError("CuratedQuery.natural_language required")
    if "sql" in data:
        out["sql"] = data["sql"]
    else:
        raise DeserializationError("CuratedQuery.sql required")
    return out
