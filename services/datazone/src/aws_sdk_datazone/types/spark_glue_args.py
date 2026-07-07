"""Generated from Smithy shape ``com.amazonaws.datazone#SparkGlueArgs``."""

from typing_extensions import NotRequired, TypedDict


class SparkGlueArgs(TypedDict, closed=True):
    connection: NotRequired["str"]
    """<p>The connection in the Spark Amazon Web Services Glue args.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkGlueArgs) -> dict:
    out: dict = {}
    if "connection" in value:
        out["connection"] = value["connection"]
    return out


def deserialize_json(data: dict) -> SparkGlueArgs:
    out: SparkGlueArgs = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        out["connection"] = data["connection"]
    return out
