"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pcs.types.cluster


class UpdateClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_pcs.types.cluster.Cluster"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_pcs.types.cluster

        out["cluster"] = aws_sdk_pcs.types.cluster.serialize_aws_json_1_0(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateClusterResponse:
    out: UpdateClusterResponse = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import aws_sdk_pcs.types.cluster

        out["cluster"] = aws_sdk_pcs.types.cluster.deserialize_aws_json_1_0(
            data["cluster"]
        )
    return out
