"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListGremlinQueriesInput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListGremlinQueriesInput(TypedDict):
    include_waiting: NotRequired["bool"]
    """<p>If set to <code>TRUE</code>, the list returned includes waiting queries. The default is <code>FALSE</code>;</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGremlinQueriesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGremlinQueriesInput:
    out: ListGremlinQueriesInput = {}  # type: ignore[typeddict-item]
    return out
