"""Generated from Smithy shape ``com.amazonaws.emr#DescribeClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster


class DescribeClusterOutput(TypedDict, closed=True):
    cluster: NotRequired["capo_emr.types.cluster.Cluster"]
    """<p>This output contains the details for the requested cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterOutput) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_emr.types.cluster

        out["Cluster"] = capo_emr.types.cluster.serialize_aws_json_1_1(value["cluster"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterOutput:
    out: DescribeClusterOutput = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import capo_emr.types.cluster

        out["cluster"] = capo_emr.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
