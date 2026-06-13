"""Generated from Smithy shape ``com.amazonaws.backupsearch#S3ExportSpecification``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_backupsearch.errors import DeserializationError


class S3ExportSpecification(TypedDict):
    destination_bucket: "str"
    """<p>This specifies the destination Amazon S3 bucket for the export job.</p>"""
    destination_prefix: NotRequired["str"]
    """<p>This specifies the prefix for the destination Amazon S3 bucket for the export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ExportSpecification) -> dict:
    out: dict = {}
    out["DestinationBucket"] = value["destination_bucket"]
    if "destination_prefix" in value:
        out["DestinationPrefix"] = value["destination_prefix"]
    return out


def deserialize_json(data: dict) -> S3ExportSpecification:
    out: S3ExportSpecification = {}  # type: ignore[typeddict-item]
    if "DestinationBucket" in data:
        out["destination_bucket"] = data["DestinationBucket"]
    else:
        raise DeserializationError("S3ExportSpecification.destination_bucket required")
    if "DestinationPrefix" in data:
        out["destination_prefix"] = data["DestinationPrefix"]
    return out
