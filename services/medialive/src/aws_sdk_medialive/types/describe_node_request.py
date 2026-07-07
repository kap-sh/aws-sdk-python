"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeNodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeNodeRequest(TypedDict, closed=True):
    cluster_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the cluster"""
    node_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the node."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNodeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeNodeRequest:
    out: DescribeNodeRequest = {}  # type: ignore[typeddict-item]
    return out
