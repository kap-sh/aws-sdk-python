"""Generated from Smithy shape ``com.amazonaws.odb#ListCloudVmClustersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class ListCloudVmClustersInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    cloud_exadata_infrastructure_id: NotRequired[
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the Oracle Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCloudVmClustersInput) -> dict:
    out: dict = {}
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCloudVmClustersInput:
    out: ListCloudVmClustersInput = {}  # type: ignore[typeddict-item]
    if "cloudExadataInfrastructureId" in data:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    return out
