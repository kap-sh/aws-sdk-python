"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeLifecycleTransition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_storage_class


class DataLakeLifecycleTransition(TypedDict):
    storage_class: NotRequired[
        "aws_sdk_securitylake.types.data_lake_storage_class.DataLakeStorageClass"
    ]
    """<p>The range of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads.</p>"""
    days: NotRequired["int"]
    """<p>Number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeLifecycleTransition) -> dict:
    out: dict = {}
    if "storage_class" in value:
        out["storageClass"] = value["storage_class"]
    if "days" in value:
        out["days"] = value["days"]
    return out


def deserialize_json(data: dict) -> DataLakeLifecycleTransition:
    out: DataLakeLifecycleTransition = {}  # type: ignore[typeddict-item]
    if "storageClass" in data:
        out["storage_class"] = data["storageClass"]
    if "days" in data:
        out["days"] = data["days"]
    return out
