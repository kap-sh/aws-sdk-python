"""Generated from Smithy shape ``com.amazonaws.dax#RebootNodeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dax.types.cluster


class RebootNodeResponse(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_dax.types.cluster.Cluster"]
    """<p>A description of the DAX cluster after a node has been rebooted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootNodeResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_dax.types.cluster

        out["Cluster"] = aws_sdk_dax.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RebootNodeResponse:
    out: RebootNodeResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import aws_sdk_dax.types.cluster

        out["cluster"] = aws_sdk_dax.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
