"""Generated from Smithy shape ``com.amazonaws.ecr#InitiateLayerUploadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.part_size
    import capo_ecr.types.upload_id


class InitiateLayerUploadResponse(TypedDict, closed=True):
    upload_id: NotRequired["capo_ecr.types.upload_id.UploadId"]
    """<p>The upload ID for the layer upload. This parameter is passed to further <a>UploadLayerPart</a> and <a>CompleteLayerUpload</a> operations.</p>"""
    part_size: NotRequired["capo_ecr.types.part_size.PartSize"]
    """<p>The size, in bytes, that Amazon ECR expects future layer part uploads to be.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InitiateLayerUploadResponse) -> dict:
    out: dict = {}
    if "upload_id" in value:
        out["uploadId"] = value["upload_id"]
    if "part_size" in value:
        out["partSize"] = value["part_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InitiateLayerUploadResponse:
    out: InitiateLayerUploadResponse = {}  # type: ignore[typeddict-item]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    if data.get("partSize") is not None:
        out["part_size"] = data["partSize"]
    return out
