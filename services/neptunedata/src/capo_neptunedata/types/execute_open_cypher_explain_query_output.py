"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteOpenCypherExplainQueryOutput``."""

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError


class ExecuteOpenCypherExplainQueryOutput(TypedDict, closed=True):
    results: "bytes"
    """<p>A text blob containing the openCypher <code>explain</code> results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteOpenCypherExplainQueryOutput) -> dict:
    out: dict = {}
    import capo_neptunedata.types._prelude.blob

    out["results"] = capo_neptunedata.types._prelude.blob.serialize_json(
        value["results"]
    )
    return out


def deserialize_json(data: dict) -> ExecuteOpenCypherExplainQueryOutput:
    out: ExecuteOpenCypherExplainQueryOutput = {}  # type: ignore[typeddict-item]
    if "results" in data:
        import capo_neptunedata.types._prelude.blob

        out["results"] = capo_neptunedata.types._prelude.blob.deserialize_json(
            data["results"]
        )
    else:
        raise DeserializationError(
            "ExecuteOpenCypherExplainQueryOutput.results required"
        )
    return out
