"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobPresignedUrlConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.expires_in_seconds


class AwsJobPresignedUrlConfig(TypedDict, closed=True):
    expires_in_sec: NotRequired["capo_iot.types.expires_in_seconds.ExpiresInSeconds"]
    """<p>How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 1800 seconds. Pre-signed URLs are generated when a request for the job document is received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobPresignedUrlConfig) -> dict:
    out: dict = {}
    if "expires_in_sec" in value:
        out["expiresInSec"] = value["expires_in_sec"]
    return out


def deserialize_json(data: dict) -> AwsJobPresignedUrlConfig:
    out: AwsJobPresignedUrlConfig = {}  # type: ignore[typeddict-item]
    if "expiresInSec" in data:
        out["expires_in_sec"] = data["expiresInSec"]
    return out
