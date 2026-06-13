"""Generated from Smithy shape ``com.amazonaws.omics#S3AccessConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.access_log_location


class S3AccessConfig(TypedDict):
    access_log_location: NotRequired[
        "aws_sdk_omics.types.access_log_location.AccessLogLocation"
    ]
    """<p>Location of the access logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3AccessConfig) -> dict:
    out: dict = {}
    if "access_log_location" in value:
        out["accessLogLocation"] = value["access_log_location"]
    return out


def deserialize_json(data: dict) -> S3AccessConfig:
    out: S3AccessConfig = {}  # type: ignore[typeddict-item]
    if "accessLogLocation" in data:
        out["access_log_location"] = data["accessLogLocation"]
    return out
