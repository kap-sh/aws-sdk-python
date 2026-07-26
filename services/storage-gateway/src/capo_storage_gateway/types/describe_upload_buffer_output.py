"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeUploadBufferOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.disk_ids
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.long


class DescribeUploadBufferOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    disk_ids: NotRequired["capo_storage_gateway.types.disk_ids.DiskIds"]
    """<p>An array of the gateway's local disk IDs that are configured as working storage. Each local disk ID is specified as a string (minimum length of 1 and maximum length of 300). If no local disks are configured as working storage, then the DiskIds array is empty.</p>"""
    upload_buffer_used_in_bytes: "capo_storage_gateway.types.long.long"
    """<p>The total number of bytes being used in the gateway's upload buffer.</p>"""
    upload_buffer_allocated_in_bytes: "capo_storage_gateway.types.long.long"
    """<p>The total number of bytes allocated in the gateway's as upload buffer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUploadBufferOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "disk_ids" in value:
        import capo_storage_gateway.types.disk_ids

        out["DiskIds"] = capo_storage_gateway.types.disk_ids.serialize_aws_json_1_1(
            value["disk_ids"]
        )
    out["UploadBufferUsedInBytes"] = value.get("upload_buffer_used_in_bytes", 0)
    out["UploadBufferAllocatedInBytes"] = value.get(
        "upload_buffer_allocated_in_bytes", 0
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUploadBufferOutput:
    out: DescribeUploadBufferOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "DiskIds" in data:
        import capo_storage_gateway.types.disk_ids

        out["disk_ids"] = capo_storage_gateway.types.disk_ids.deserialize_aws_json_1_1(
            data["DiskIds"]
        )
    if "UploadBufferUsedInBytes" in data:
        out["upload_buffer_used_in_bytes"] = data["UploadBufferUsedInBytes"]
    else:
        out["upload_buffer_used_in_bytes"] = 0
    if "UploadBufferAllocatedInBytes" in data:
        out["upload_buffer_allocated_in_bytes"] = data["UploadBufferAllocatedInBytes"]
    else:
        out["upload_buffer_allocated_in_bytes"] = 0
    return out
