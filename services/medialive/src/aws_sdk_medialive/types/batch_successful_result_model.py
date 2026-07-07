"""Generated from Smithy shape ``com.amazonaws.medialive#BatchSuccessfulResultModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class BatchSuccessfulResultModel(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """ARN of the resource"""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """ID of the resource"""
    state: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Current state of the resource"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchSuccessfulResultModel) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "state" in value:
        out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> BatchSuccessfulResultModel:
    out: BatchSuccessfulResultModel = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "state" in data:
        out["state"] = data["state"]
    return out
