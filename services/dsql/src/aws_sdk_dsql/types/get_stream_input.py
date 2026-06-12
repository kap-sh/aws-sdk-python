"""Generated from Smithy shape ``com.amazonaws.dsql#GetStreamInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.stream_id

class GetStreamInput(TypedDict):
    cluster_identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster containing the stream to retrieve.</p>"""
    stream_identifier: "aws_sdk_dsql.types.stream_id.StreamId"
    """<p>The ID of the stream to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetStreamInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStreamInput:
    out: GetStreamInput = {}  # type: ignore[typeddict-item]
    return out