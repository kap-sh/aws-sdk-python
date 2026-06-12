"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ModifyClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.cluster


class ModifyClusterResponse(TypedDict):
    cluster: NotRequired["aws_sdk_cloudhsm_v2.types.cluster.Cluster"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_cloudhsm_v2.types.cluster

        out["Cluster"] = aws_sdk_cloudhsm_v2.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyClusterResponse:
    out: ModifyClusterResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import aws_sdk_cloudhsm_v2.types.cluster

        out["cluster"] = aws_sdk_cloudhsm_v2.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
