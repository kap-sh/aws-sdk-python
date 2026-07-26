"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetOpenCypherQueryStatusInput``."""

from typing_extensions import TypedDict


class GetOpenCypherQueryStatusInput(TypedDict, closed=True):
    query_id: "str"
    """<p>The unique ID of the openCypher query for which to retrieve the query status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOpenCypherQueryStatusInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOpenCypherQueryStatusInput:
    out: GetOpenCypherQueryStatusInput = {}  # type: ignore[typeddict-item]
    return out
