"""Generated from Smithy shape ``com.amazonaws.docdbelastic#StartClusterInput``."""

from typing import TypedDict


class StartClusterInput(TypedDict):
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartClusterInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartClusterInput:
    out: StartClusterInput = {}  # type: ignore[typeddict-item]
    return out
