"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.cluster


class UpdateClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_memorydb.types.cluster.Cluster"]
    """<p>The updated cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_memorydb.types.cluster

        out["Cluster"] = aws_sdk_memorydb.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterResponse:
    out: UpdateClusterResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import aws_sdk_memorydb.types.cluster

        out["cluster"] = aws_sdk_memorydb.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
