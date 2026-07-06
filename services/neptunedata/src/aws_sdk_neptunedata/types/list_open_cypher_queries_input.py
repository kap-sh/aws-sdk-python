"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListOpenCypherQueriesInput``."""

from typing_extensions import NotRequired, TypedDict


class ListOpenCypherQueriesInput(TypedDict, closed=True):
    include_waiting: NotRequired["bool"]
    """<p> When set to <code>TRUE</code> and other parameters are not present, causes status information to be returned for waiting queries as well as for running queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOpenCypherQueriesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOpenCypherQueriesInput:
    out: ListOpenCypherQueriesInput = {}  # type: ignore[typeddict-item]
    return out
