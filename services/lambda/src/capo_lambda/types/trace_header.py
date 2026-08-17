"""Generated from Smithy shape ``com.amazonaws.lambda#TraceHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.x_amzn_trace_id


class TraceHeader(TypedDict, closed=True):
    x_amzn_trace_id: NotRequired["capo_lambda.types.x_amzn_trace_id.XAmznTraceId"]
    """<p>The X-Ray trace header associated with the durable execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TraceHeader) -> dict:
    out: dict = {}
    if "x_amzn_trace_id" in value:
        out["XAmznTraceId"] = value["x_amzn_trace_id"]
    return out


def deserialize_json(data: dict) -> TraceHeader:
    out: TraceHeader = {}  # type: ignore[typeddict-item]
    if data.get("XAmznTraceId") is not None:
        out["x_amzn_trace_id"] = data["XAmznTraceId"]
    return out
