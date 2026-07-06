"""Generated from Smithy shape ``com.amazonaws.ecs#CreateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster


class CreateClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_ecs.types.cluster.Cluster"]
    """<p>The full description of your new cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_ecs.types.cluster

        out["cluster"] = aws_sdk_ecs.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterResponse:
    out: CreateClusterResponse = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import aws_sdk_ecs.types.cluster

        out["cluster"] = aws_sdk_ecs.types.cluster.deserialize_aws_json_1_1(
            data["cluster"]
        )
    return out
