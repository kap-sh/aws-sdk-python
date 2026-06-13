"""Generated from Smithy shape ``com.amazonaws.dsql#MultiRegionProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_arn_list
    import aws_sdk_dsql.types.region


class MultiRegionProperties(TypedDict):
    witness_region: NotRequired["aws_sdk_dsql.types.region.Region"]
    """<p>The Region that serves as the witness region for a multi-Region cluster. The witness Region helps maintain cluster consistency and quorum.</p>"""
    clusters: NotRequired["aws_sdk_dsql.types.cluster_arn_list.ClusterArnList"]
    """<p>The set of peered clusters that form the multi-Region cluster configuration. Each peered cluster represents a database instance in a different Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiRegionProperties) -> dict:
    out: dict = {}
    if "witness_region" in value:
        out["witnessRegion"] = value["witness_region"]
    if "clusters" in value:
        import aws_sdk_dsql.types.cluster_arn_list

        out["clusters"] = aws_sdk_dsql.types.cluster_arn_list.serialize_json(
            value["clusters"]
        )
    return out


def deserialize_json(data: dict) -> MultiRegionProperties:
    out: MultiRegionProperties = {}  # type: ignore[typeddict-item]
    if "witnessRegion" in data:
        out["witness_region"] = data["witnessRegion"]
    if "clusters" in data:
        import aws_sdk_dsql.types.cluster_arn_list

        out["clusters"] = aws_sdk_dsql.types.cluster_arn_list.deserialize_json(
            data["clusters"]
        )
    return out
