"""Generated from Smithy shape ``com.amazonaws.licensemanager#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class S3Location(TypedDict, closed=True):
    bucket: NotRequired["capo_license_manager.types.string.String"]
    """<p>Name of the S3 bucket reports are published to.</p>"""
    key_prefix: NotRequired["capo_license_manager.types.string.String"]
    """<p>Prefix of the S3 bucket reports are published to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    return out
