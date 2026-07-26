"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.gremlin_query_status_attributes


class ExecuteGremlinQueryOutput(TypedDict, closed=True):
    request_id: NotRequired["str"]
    """<p>The unique identifier of the Gremlin query.</p>"""
    status: NotRequired[
        "capo_neptunedata.types.gremlin_query_status_attributes.GremlinQueryStatusAttributes"
    ]
    """<p>The status of the Gremlin query.</p>"""
    result: NotRequired["object"]
    """<p>The Gremlin query output from the server.</p>"""
    meta: NotRequired["object"]
    """<p>Metadata about the Gremlin query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteGremlinQueryOutput) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "status" in value:
        import capo_neptunedata.types.gremlin_query_status_attributes

        out["status"] = (
            capo_neptunedata.types.gremlin_query_status_attributes.serialize_json(
                value["status"]
            )
        )
    if "result" in value:
        out["result"] = value["result"]
    if "meta" in value:
        out["meta"] = value["meta"]
    return out


def deserialize_json(data: dict) -> ExecuteGremlinQueryOutput:
    out: ExecuteGremlinQueryOutput = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "status" in data:
        import capo_neptunedata.types.gremlin_query_status_attributes

        out["status"] = (
            capo_neptunedata.types.gremlin_query_status_attributes.deserialize_json(
                data["status"]
            )
        )
    if "result" in data:
        out["result"] = data["result"]
    if "meta" in data:
        out["meta"] = data["meta"]
    return out
