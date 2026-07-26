"""Generated from Smithy shape ``com.amazonaws.quicksight#TwitterParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.positive_integer
    import capo_quicksight.types.query


class TwitterParameters(TypedDict, closed=True):
    query: "capo_quicksight.types.query.Query"
    """<p>Twitter query string.</p>"""
    max_rows: "capo_quicksight.types.positive_integer.PositiveInteger"
    """<p>Maximum number of rows to query Twitter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TwitterParameters) -> dict:
    out: dict = {}
    out["Query"] = value["query"]
    out["MaxRows"] = value["max_rows"]
    return out


def deserialize_json(data: dict) -> TwitterParameters:
    out: TwitterParameters = {}  # type: ignore[typeddict-item]
    if "Query" in data:
        out["query"] = data["Query"]
    else:
        raise DeserializationError("TwitterParameters.query required")
    if "MaxRows" in data:
        out["max_rows"] = data["MaxRows"]
    else:
        raise DeserializationError("TwitterParameters.max_rows required")
    return out
