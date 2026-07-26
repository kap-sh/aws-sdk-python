"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeStorageVirtualMachinesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.max_results
    import capo_fsx.types.next_token
    import capo_fsx.types.storage_virtual_machine_filters
    import capo_fsx.types.storage_virtual_machine_ids


class DescribeStorageVirtualMachinesRequest(TypedDict, closed=True):
    storage_virtual_machine_ids: NotRequired[
        "capo_fsx.types.storage_virtual_machine_ids.StorageVirtualMachineIds"
    ]
    """<p>Enter the ID of one or more SVMs that you want to view.</p>"""
    filters: NotRequired[
        "capo_fsx.types.storage_virtual_machine_filters.StorageVirtualMachineFilters"
    ]
    """<p>Enter a filter name:value pair to view a select set of SVMs.</p>"""
    max_results: NotRequired["capo_fsx.types.max_results.MaxResults"]
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStorageVirtualMachinesRequest) -> dict:
    out: dict = {}
    if "storage_virtual_machine_ids" in value:
        import capo_fsx.types.storage_virtual_machine_ids

        out["StorageVirtualMachineIds"] = (
            capo_fsx.types.storage_virtual_machine_ids.serialize_aws_json_1_1(
                value["storage_virtual_machine_ids"]
            )
        )
    if "filters" in value:
        import capo_fsx.types.storage_virtual_machine_filters

        out["Filters"] = (
            capo_fsx.types.storage_virtual_machine_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStorageVirtualMachinesRequest:
    out: DescribeStorageVirtualMachinesRequest = {}  # type: ignore[typeddict-item]
    if "StorageVirtualMachineIds" in data:
        import capo_fsx.types.storage_virtual_machine_ids

        out["storage_virtual_machine_ids"] = (
            capo_fsx.types.storage_virtual_machine_ids.deserialize_aws_json_1_1(
                data["StorageVirtualMachineIds"]
            )
        )
    if "Filters" in data:
        import capo_fsx.types.storage_virtual_machine_filters

        out["filters"] = (
            capo_fsx.types.storage_virtual_machine_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
