"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_applicationcostprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.s3_bucket
    import capo_applicationcostprofiler.types.s3_prefix


class S3Location(TypedDict, closed=True):
    bucket: "capo_applicationcostprofiler.types.s3_bucket.S3Bucket"
    """<p>Name of the S3 bucket.</p>"""
    prefix: "capo_applicationcostprofiler.types.s3_prefix.S3Prefix"
    """<p>Prefix for the location to write to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("S3Location.bucket required")
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    else:
        raise DeserializationError("S3Location.prefix required")
    return out
