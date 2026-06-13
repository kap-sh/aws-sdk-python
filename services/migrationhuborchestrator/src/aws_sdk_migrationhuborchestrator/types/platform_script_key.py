"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#PlatformScriptKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.s3_key


class PlatformScriptKey(TypedDict):
    linux: NotRequired["aws_sdk_migrationhuborchestrator.types.s3_key.S3Key"]
    """<p>The script location for Linux.</p>"""
    windows: NotRequired["aws_sdk_migrationhuborchestrator.types.s3_key.S3Key"]
    """<p>The script location for Windows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlatformScriptKey) -> dict:
    out: dict = {}
    if "linux" in value:
        out["linux"] = value["linux"]
    if "windows" in value:
        out["windows"] = value["windows"]
    return out


def deserialize_json(data: dict) -> PlatformScriptKey:
    out: PlatformScriptKey = {}  # type: ignore[typeddict-item]
    if "linux" in data:
        out["linux"] = data["linux"]
    if "windows" in data:
        out["windows"] = data["windows"]
    return out
