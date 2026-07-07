"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateStorageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.provisioned_throughput
    import aws_sdk_kafka.types.storage_mode


class UpdateStorageRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of cluster to update from. A successful operation will then generate a new version.</p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_kafka.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>EBS volume provisioned throughput information.</p>"""
    storage_mode: NotRequired["aws_sdk_kafka.types.storage_mode.StorageMode"]
    """<p>Controls storage mode for supported storage tiers.</p>"""
    volume_size_gb: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>size of the EBS volume to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStorageRequest) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "provisioned_throughput" in value:
        import aws_sdk_kafka.types.provisioned_throughput

        out["provisionedThroughput"] = (
            aws_sdk_kafka.types.provisioned_throughput.serialize_json(
                value["provisioned_throughput"]
            )
        )
    if "storage_mode" in value:
        import aws_sdk_kafka.types.storage_mode

        out["storageMode"] = aws_sdk_kafka.types.storage_mode.serialize_json(
            value["storage_mode"]
        )
    if "volume_size_gb" in value:
        out["volumeSizeGB"] = value["volume_size_gb"]
    return out


def deserialize_json(data: dict) -> UpdateStorageRequest:
    out: UpdateStorageRequest = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "provisionedThroughput" in data:
        import aws_sdk_kafka.types.provisioned_throughput

        out["provisioned_throughput"] = (
            aws_sdk_kafka.types.provisioned_throughput.deserialize_json(
                data["provisionedThroughput"]
            )
        )
    if "storageMode" in data:
        import aws_sdk_kafka.types.storage_mode

        out["storage_mode"] = aws_sdk_kafka.types.storage_mode.deserialize_json(
            data["storageMode"]
        )
    if "volumeSizeGB" in data:
        out["volume_size_gb"] = data["volumeSizeGB"]
    return out
