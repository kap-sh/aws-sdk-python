"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteOpenCypherExplainQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.open_cypher_explain_mode


class ExecuteOpenCypherExplainQueryInput(TypedDict, closed=True):
    open_cypher_query: "str"
    """<p>The openCypher query string.</p>"""
    parameters: NotRequired["str"]
    """<p>The openCypher query parameters.</p>"""
    explain_mode: (
        "aws_sdk_neptunedata.types.open_cypher_explain_mode.OpenCypherExplainMode"
    )
    """<p>The openCypher <code>explain</code> mode. Can be one of: <code>static</code>, <code>dynamic</code>, or <code>details</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteOpenCypherExplainQueryInput) -> dict:
    out: dict = {}
    out["query"] = value["open_cypher_query"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    import aws_sdk_neptunedata.types.open_cypher_explain_mode

    out["explain"] = aws_sdk_neptunedata.types.open_cypher_explain_mode.serialize_json(
        value["explain_mode"]
    )
    return out


def deserialize_json(data: dict) -> ExecuteOpenCypherExplainQueryInput:
    out: ExecuteOpenCypherExplainQueryInput = {}  # type: ignore[typeddict-item]
    if "query" in data:
        out["open_cypher_query"] = data["query"]
    else:
        raise DeserializationError(
            "ExecuteOpenCypherExplainQueryInput.open_cypher_query required"
        )
    if "parameters" in data:
        out["parameters"] = data["parameters"]
    if "explain" in data:
        import aws_sdk_neptunedata.types.open_cypher_explain_mode

        out["explain_mode"] = (
            aws_sdk_neptunedata.types.open_cypher_explain_mode.deserialize_json(
                data["explain"]
            )
        )
    else:
        raise DeserializationError(
            "ExecuteOpenCypherExplainQueryInput.explain_mode required"
        )
    return out
