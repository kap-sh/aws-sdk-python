"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetPropertygraphSummaryInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.graph_summary_type


class GetPropertygraphSummaryInput(TypedDict):
    mode: "aws_sdk_neptunedata.types.graph_summary_type.GraphSummaryType"
    """<p>Mode can take one of two values: <code>BASIC</code> (the default), and <code>DETAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertygraphSummaryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPropertygraphSummaryInput:
    out: GetPropertygraphSummaryInput = {}  # type: ignore[typeddict-item]
    return out
