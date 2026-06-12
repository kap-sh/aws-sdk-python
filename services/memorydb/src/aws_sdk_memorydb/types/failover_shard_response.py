"""Generated from Smithy shape ``com.amazonaws.memorydb#FailoverShardResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.cluster


class FailoverShardResponse(TypedDict):
    cluster: NotRequired["aws_sdk_memorydb.types.cluster.Cluster"]
    """<p>The cluster being failed over.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailoverShardResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_memorydb.types.cluster

        out["Cluster"] = aws_sdk_memorydb.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailoverShardResponse:
    out: FailoverShardResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import aws_sdk_memorydb.types.cluster

        out["cluster"] = aws_sdk_memorydb.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
