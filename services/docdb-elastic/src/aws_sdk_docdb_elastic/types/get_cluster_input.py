"""Generated from Smithy shape ``com.amazonaws.docdbelastic#GetClusterInput``."""

from typing import TypedDict


class GetClusterInput(TypedDict):
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetClusterInput:
    out: GetClusterInput = {}  # type: ignore[typeddict-item]
    return out
