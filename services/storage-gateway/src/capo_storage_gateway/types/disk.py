"""Generated from Smithy shape ``com.amazonaws.storagegateway#Disk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.disk_allocation_type
    import capo_storage_gateway.types.disk_attribute_list
    import capo_storage_gateway.types.disk_id
    import capo_storage_gateway.types.long
    import capo_storage_gateway.types.string


class Disk(TypedDict, closed=True):
    disk_id: NotRequired["capo_storage_gateway.types.disk_id.DiskId"]
    """<p>The unique device ID or other distinguishing data that identifies a local disk.</p>"""
    disk_path: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>The path of a local disk in the gateway virtual machine (VM).</p>"""
    disk_node: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>The device node of a local disk as assigned by the virtualization environment.</p>"""
    disk_status: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>A value that represents the status of a local disk.</p>"""
    disk_size_in_bytes: "capo_storage_gateway.types.long.long"
    """<p>The local disk size in bytes.</p>"""
    disk_allocation_type: NotRequired[
        "capo_storage_gateway.types.disk_allocation_type.DiskAllocationType"
    ]
    disk_allocation_resource: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>The iSCSI qualified name (IQN) that is defined for a disk. This field is not included in the response if the local disk is not defined as an iSCSI target. The format of this field is <i>targetIqn::LUNNumber::region-volumeId</i>.</p>"""
    disk_attribute_list: NotRequired[
        "capo_storage_gateway.types.disk_attribute_list.DiskAttributeList"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Disk) -> dict:
    out: dict = {}
    if "disk_id" in value:
        out["DiskId"] = value["disk_id"]
    if "disk_path" in value:
        out["DiskPath"] = value["disk_path"]
    if "disk_node" in value:
        out["DiskNode"] = value["disk_node"]
    if "disk_status" in value:
        out["DiskStatus"] = value["disk_status"]
    out["DiskSizeInBytes"] = value.get("disk_size_in_bytes", 0)
    if "disk_allocation_type" in value:
        out["DiskAllocationType"] = value["disk_allocation_type"]
    if "disk_allocation_resource" in value:
        out["DiskAllocationResource"] = value["disk_allocation_resource"]
    if "disk_attribute_list" in value:
        import capo_storage_gateway.types.disk_attribute_list

        out["DiskAttributeList"] = (
            capo_storage_gateway.types.disk_attribute_list.serialize_aws_json_1_1(
                value["disk_attribute_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Disk:
    out: Disk = {}  # type: ignore[typeddict-item]
    if "DiskId" in data:
        out["disk_id"] = data["DiskId"]
    if "DiskPath" in data:
        out["disk_path"] = data["DiskPath"]
    if "DiskNode" in data:
        out["disk_node"] = data["DiskNode"]
    if "DiskStatus" in data:
        out["disk_status"] = data["DiskStatus"]
    if "DiskSizeInBytes" in data:
        out["disk_size_in_bytes"] = data["DiskSizeInBytes"]
    else:
        out["disk_size_in_bytes"] = 0
    if "DiskAllocationType" in data:
        out["disk_allocation_type"] = data["DiskAllocationType"]
    if "DiskAllocationResource" in data:
        out["disk_allocation_resource"] = data["DiskAllocationResource"]
    if "DiskAttributeList" in data:
        import capo_storage_gateway.types.disk_attribute_list

        out["disk_attribute_list"] = (
            capo_storage_gateway.types.disk_attribute_list.deserialize_aws_json_1_1(
                data["DiskAttributeList"]
            )
        )
    return out
