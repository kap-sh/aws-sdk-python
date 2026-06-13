"""Generated from Smithy shape ``com.amazonaws.emr#DescribeClusterOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster


class DescribeClusterOutput(TypedDict):
    cluster: NotRequired["aws_sdk_emr.types.cluster.Cluster"]
    """<p>This output contains the details for the requested cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterOutput) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_emr.types.cluster

        out["Cluster"] = aws_sdk_emr.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterOutput:
    out: DescribeClusterOutput = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import aws_sdk_emr.types.cluster

        out["cluster"] = aws_sdk_emr.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
