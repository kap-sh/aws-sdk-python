"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeStorageVirtualMachinesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.next_token
    import capo_fsx.types.storage_virtual_machines


class DescribeStorageVirtualMachinesResponse(TypedDict, closed=True):
    storage_virtual_machines: NotRequired[
        "capo_fsx.types.storage_virtual_machines.StorageVirtualMachines"
    ]
    """<p>Returned after a successful <code>DescribeStorageVirtualMachines</code> operation, describing each SVM.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStorageVirtualMachinesResponse) -> dict:
    out: dict = {}
    if "storage_virtual_machines" in value:
        import capo_fsx.types.storage_virtual_machines

        out["StorageVirtualMachines"] = (
            capo_fsx.types.storage_virtual_machines.serialize_aws_json_1_1(
                value["storage_virtual_machines"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStorageVirtualMachinesResponse:
    out: DescribeStorageVirtualMachinesResponse = {}  # type: ignore[typeddict-item]
    if "StorageVirtualMachines" in data:
        import capo_fsx.types.storage_virtual_machines

        out["storage_virtual_machines"] = (
            capo_fsx.types.storage_virtual_machines.deserialize_aws_json_1_1(
                data["StorageVirtualMachines"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
