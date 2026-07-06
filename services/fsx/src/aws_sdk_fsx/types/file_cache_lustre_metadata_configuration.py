"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheLustreMetadataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.metadata_storage_capacity


class FileCacheLustreMetadataConfiguration(TypedDict, closed=True):
    storage_capacity: NotRequired[
        "aws_sdk_fsx.types.metadata_storage_capacity.MetadataStorageCapacity"
    ]
    """<p>The storage capacity of the Lustre MDT (Metadata Target) storage volume in gibibytes (GiB). The only supported value is <code>2400</code> GiB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheLustreMetadataConfiguration) -> dict:
    out: dict = {}
    if "storage_capacity" in value:
        out["StorageCapacity"] = value["storage_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileCacheLustreMetadataConfiguration:
    out: FileCacheLustreMetadataConfiguration = {}  # type: ignore[typeddict-item]
    if "StorageCapacity" in data:
        out["storage_capacity"] = data["StorageCapacity"]
    return out
