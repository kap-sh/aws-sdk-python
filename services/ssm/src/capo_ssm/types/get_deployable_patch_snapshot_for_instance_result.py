"""Generated from Smithy shape ``com.amazonaws.ssm#GetDeployablePatchSnapshotForInstanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_id
    import capo_ssm.types.product
    import capo_ssm.types.snapshot_download_url
    import capo_ssm.types.snapshot_id


class GetDeployablePatchSnapshotForInstanceResult(TypedDict, closed=True):
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID.</p>"""
    snapshot_id: NotRequired["capo_ssm.types.snapshot_id.SnapshotId"]
    """<p>The user-defined snapshot ID.</p>"""
    snapshot_download_url: NotRequired[
        "capo_ssm.types.snapshot_download_url.SnapshotDownloadUrl"
    ]
    """<p>A pre-signed Amazon Simple Storage Service (Amazon S3) URL that can be used to download the patch snapshot.</p>"""
    product: NotRequired["capo_ssm.types.product.Product"]
    """<p>Returns the specific operating system (for example Windows Server 2012 or Amazon Linux 2015.09) on the managed node for the specified patch snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeployablePatchSnapshotForInstanceResult) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "snapshot_download_url" in value:
        out["SnapshotDownloadUrl"] = value["snapshot_download_url"]
    if "product" in value:
        out["Product"] = value["product"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeployablePatchSnapshotForInstanceResult:
    out: GetDeployablePatchSnapshotForInstanceResult = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    if "SnapshotDownloadUrl" in data:
        out["snapshot_download_url"] = data["SnapshotDownloadUrl"]
    if "Product" in data:
        out["product"] = data["Product"]
    return out
