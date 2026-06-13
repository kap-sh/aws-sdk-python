"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#AuroraDbClusterStorageConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AuroraDbClusterStorageConfiguration(TypedDict):
    storage_type: NotRequired["str"]
    """<p>The storage type to associate with the Aurora DB cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AuroraDbClusterStorageConfiguration) -> dict:
    out: dict = {}
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AuroraDbClusterStorageConfiguration:
    out: AuroraDbClusterStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    return out
