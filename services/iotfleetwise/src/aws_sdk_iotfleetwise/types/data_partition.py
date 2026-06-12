"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataPartition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.data_partition_id
    import aws_sdk_iotfleetwise.types.data_partition_storage_options
    import aws_sdk_iotfleetwise.types.data_partition_upload_options


class DataPartition(TypedDict):
    id: "aws_sdk_iotfleetwise.types.data_partition_id.DataPartitionId"
    """<p>The ID of the data partition. The data partition ID must be unique within a campaign. You can establish a data partition as the default partition for a campaign by using <code>default</code> as the ID.</p>"""
    storage_options: "aws_sdk_iotfleetwise.types.data_partition_storage_options.DataPartitionStorageOptions"
    """<p>The storage options for a data partition.</p>"""
    upload_options: NotRequired[
        "aws_sdk_iotfleetwise.types.data_partition_upload_options.DataPartitionUploadOptions"
    ]
    """<p>The upload options for the data partition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataPartition) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_iotfleetwise.types.data_partition_storage_options

    out["storageOptions"] = (
        aws_sdk_iotfleetwise.types.data_partition_storage_options.serialize_aws_json_1_0(
            value["storage_options"]
        )
    )
    if "upload_options" in value:
        import aws_sdk_iotfleetwise.types.data_partition_upload_options

        out["uploadOptions"] = (
            aws_sdk_iotfleetwise.types.data_partition_upload_options.serialize_aws_json_1_0(
                value["upload_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DataPartition:
    out: DataPartition = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DataPartition.id required")
    if "storageOptions" in data:
        import aws_sdk_iotfleetwise.types.data_partition_storage_options

        out["storage_options"] = (
            aws_sdk_iotfleetwise.types.data_partition_storage_options.deserialize_aws_json_1_0(
                data["storageOptions"]
            )
        )
    else:
        raise DeserializationError("DataPartition.storage_options required")
    if "uploadOptions" in data:
        import aws_sdk_iotfleetwise.types.data_partition_upload_options

        out["upload_options"] = (
            aws_sdk_iotfleetwise.types.data_partition_upload_options.deserialize_aws_json_1_0(
                data["uploadOptions"]
            )
        )
    return out
