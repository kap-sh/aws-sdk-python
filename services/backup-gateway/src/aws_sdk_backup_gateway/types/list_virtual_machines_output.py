"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListVirtualMachinesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.next_token
    import aws_sdk_backup_gateway.types.virtual_machines


class ListVirtualMachinesOutput(TypedDict):
    virtual_machines: NotRequired[
        "aws_sdk_backup_gateway.types.virtual_machines.VirtualMachines"
    ]
    """<p>A list of your <code>VirtualMachine</code> objects, ordered by their Amazon Resource Names (ARNs).</p>"""
    next_token: NotRequired["aws_sdk_backup_gateway.types.next_token.NextToken"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVirtualMachinesOutput) -> dict:
    out: dict = {}
    if "virtual_machines" in value:
        import aws_sdk_backup_gateway.types.virtual_machines

        out["VirtualMachines"] = (
            aws_sdk_backup_gateway.types.virtual_machines.serialize_aws_json_1_0(
                value["virtual_machines"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVirtualMachinesOutput:
    out: ListVirtualMachinesOutput = {}  # type: ignore[typeddict-item]
    if "VirtualMachines" in data:
        import aws_sdk_backup_gateway.types.virtual_machines

        out["virtual_machines"] = (
            aws_sdk_backup_gateway.types.virtual_machines.deserialize_aws_json_1_0(
                data["VirtualMachines"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
