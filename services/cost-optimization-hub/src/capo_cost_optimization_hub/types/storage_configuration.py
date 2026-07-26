"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#StorageConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class StorageConfiguration(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The storage type.</p>"""
    size_in_gb: NotRequired["float"]
    """<p>The storage volume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StorageConfiguration:
    out: StorageConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    return out
