"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#S3SourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.s3_source_location


class S3SourceConfiguration(TypedDict, closed=True):
    location: "aws_sdk_iottwinmaker.types.s3_source_location.S3SourceLocation"
    """<p>The S3 destination source configuration location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3SourceConfiguration) -> dict:
    out: dict = {}
    out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> S3SourceConfiguration:
    out: S3SourceConfiguration = {}  # type: ignore[typeddict-item]
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError("S3SourceConfiguration.location required")
    return out
