"""Generated from Smithy shape ``com.amazonaws.docdbelastic#StopClusterInput``."""

from typing import TypedDict


class StopClusterInput(TypedDict):
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopClusterInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopClusterInput:
    out: StopClusterInput = {}  # type: ignore[typeddict-item]
    return out
