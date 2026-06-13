"""Generated from Smithy shape ``com.amazonaws.cleanrooms#S3Location``."""

from typing import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError


class S3Location(TypedDict):
    bucket: "str"
    """<p> The bucket name.</p>"""
    key: "str"
    """<p> The object key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("S3Location.bucket required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3Location.key required")
    return out
