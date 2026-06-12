"""Generated from Smithy shape ``com.amazonaws.medialive#BatchFailedResultModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class BatchFailedResultModel(TypedDict):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """ARN of the resource"""
    code: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Error code for the failed operation"""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """ID of the resource"""
    message: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Error message for the failed operation"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchFailedResultModel) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "code" in value:
        out["code"] = value["code"]
    if "id" in value:
        out["id"] = value["id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchFailedResultModel:
    out: BatchFailedResultModel = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "code" in data:
        out["code"] = data["code"]
    if "id" in data:
        out["id"] = data["id"]
    if "message" in data:
        out["message"] = data["message"]
    return out
