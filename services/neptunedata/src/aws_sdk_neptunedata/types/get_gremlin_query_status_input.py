"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetGremlinQueryStatusInput``."""

from typing import TypedDict


class GetGremlinQueryStatusInput(TypedDict):
    query_id: "str"
    """<p>The unique identifier that identifies the Gremlin query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGremlinQueryStatusInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGremlinQueryStatusInput:
    out: GetGremlinQueryStatusInput = {}  # type: ignore[typeddict-item]
    return out
