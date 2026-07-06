"""Generated from Smithy shape ``com.amazonaws.appflow#S3Metadata``."""

from typing_extensions import TypedDict


class S3Metadata(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: S3Metadata) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> S3Metadata:
    out: S3Metadata = {}  # type: ignore[typeddict-item]
    return out
