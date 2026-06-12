"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterSummary``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dsql.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_arn
    import aws_sdk_dsql.types.cluster_id

class ClusterSummary(TypedDict):
    identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster.</p>"""
    arn: "aws_sdk_dsql.types.cluster_arn.ClusterArn"
    """<p>The ARN of the cluster.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ClusterSummary) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ClusterSummary:
    out: ClusterSummary = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("ClusterSummary.identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ClusterSummary.arn required")
    return out