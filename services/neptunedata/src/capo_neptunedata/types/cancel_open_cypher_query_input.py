"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelOpenCypherQueryInput``."""

from typing_extensions import NotRequired, TypedDict


class CancelOpenCypherQueryInput(TypedDict, closed=True):
    query_id: "str"
    """<p>The unique ID of the openCypher query to cancel.</p>"""
    silent: NotRequired["bool"]
    """<p>If set to <code>TRUE</code>, causes the cancelation of the openCypher query to happen silently.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelOpenCypherQueryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelOpenCypherQueryInput:
    out: CancelOpenCypherQueryInput = {}  # type: ignore[typeddict-item]
    return out
