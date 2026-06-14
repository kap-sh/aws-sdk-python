"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeWorkingStorageOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.disk_ids
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.long


class DescribeWorkingStorageOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    disk_ids: NotRequired["aws_sdk_storage_gateway.types.disk_ids.DiskIds"]
    """<p>An array of the gateway's local disk IDs that are configured as working storage. Each local disk ID is specified as a string (minimum length of 1 and maximum length of 300). If no local disks are configured as working storage, then the DiskIds array is empty.</p>"""
    working_storage_used_in_bytes: "aws_sdk_storage_gateway.types.long.long"
    """<p>The total working storage in bytes in use by the gateway. If no working storage is configured for the gateway, this field returns 0.</p>"""
    working_storage_allocated_in_bytes: "aws_sdk_storage_gateway.types.long.long"
    """<p>The total working storage in bytes allocated for the gateway. If no working storage is configured for the gateway, this field returns 0.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkingStorageOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "disk_ids" in value:
        import aws_sdk_storage_gateway.types.disk_ids

        out["DiskIds"] = aws_sdk_storage_gateway.types.disk_ids.serialize_aws_json_1_1(
            value["disk_ids"]
        )
    out["WorkingStorageUsedInBytes"] = value.get("working_storage_used_in_bytes", 0)
    out["WorkingStorageAllocatedInBytes"] = value.get(
        "working_storage_allocated_in_bytes", 0
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkingStorageOutput:
    out: DescribeWorkingStorageOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "DiskIds" in data:
        import aws_sdk_storage_gateway.types.disk_ids

        out["disk_ids"] = (
            aws_sdk_storage_gateway.types.disk_ids.deserialize_aws_json_1_1(
                data["DiskIds"]
            )
        )
    if "WorkingStorageUsedInBytes" in data:
        out["working_storage_used_in_bytes"] = data["WorkingStorageUsedInBytes"]
    else:
        out["working_storage_used_in_bytes"] = 0
    if "WorkingStorageAllocatedInBytes" in data:
        out["working_storage_allocated_in_bytes"] = data[
            "WorkingStorageAllocatedInBytes"
        ]
    else:
        out["working_storage_allocated_in_bytes"] = 0
    return out
