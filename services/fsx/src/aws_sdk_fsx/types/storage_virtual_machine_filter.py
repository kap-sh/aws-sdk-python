"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.storage_virtual_machine_filter_name
    import aws_sdk_fsx.types.storage_virtual_machine_filter_values


class StorageVirtualMachineFilter(TypedDict):
    name: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_filter_name.StorageVirtualMachineFilterName"
    ]
    """<p>The name for this filter.</p>"""
    values: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_filter_values.StorageVirtualMachineFilterValues"
    ]
    """<p>The values of the filter. These are all the values for any of the applied filters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachineFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_fsx.types.storage_virtual_machine_filter_name

        out["Name"] = (
            aws_sdk_fsx.types.storage_virtual_machine_filter_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "values" in value:
        import aws_sdk_fsx.types.storage_virtual_machine_filter_values

        out["Values"] = (
            aws_sdk_fsx.types.storage_virtual_machine_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageVirtualMachineFilter:
    out: StorageVirtualMachineFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_fsx.types.storage_virtual_machine_filter_name

        out["name"] = (
            aws_sdk_fsx.types.storage_virtual_machine_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "Values" in data:
        import aws_sdk_fsx.types.storage_virtual_machine_filter_values

        out["values"] = (
            aws_sdk_fsx.types.storage_virtual_machine_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
