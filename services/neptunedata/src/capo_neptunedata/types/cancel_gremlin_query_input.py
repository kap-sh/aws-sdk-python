"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelGremlinQueryInput``."""

from typing_extensions import TypedDict


class CancelGremlinQueryInput(TypedDict, closed=True):
    query_id: "str"
    """<p>The unique identifier that identifies the query to be canceled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelGremlinQueryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelGremlinQueryInput:
    out: CancelGremlinQueryInput = {}  # type: ignore[typeddict-item]
    return out
