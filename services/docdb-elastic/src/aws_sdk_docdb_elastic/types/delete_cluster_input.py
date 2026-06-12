"""Generated from Smithy shape ``com.amazonaws.docdbelastic#DeleteClusterInput``."""

from typing import TypedDict


class DeleteClusterInput(TypedDict):
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster that is to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterInput:
    out: DeleteClusterInput = {}  # type: ignore[typeddict-item]
    return out
