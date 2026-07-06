"""Generated from Smithy shape ``com.amazonaws.resiliencehub#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.string500


class S3Location(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>The name of the Amazon S3 bucket.</p>"""
    prefix: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>The prefix for the Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
