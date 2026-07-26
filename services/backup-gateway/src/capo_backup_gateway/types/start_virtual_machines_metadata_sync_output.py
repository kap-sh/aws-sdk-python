"""Generated from Smithy shape ``com.amazonaws.backupgateway#StartVirtualMachinesMetadataSyncOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.server_arn


class StartVirtualMachinesMetadataSyncOutput(TypedDict, closed=True):
    hypervisor_arn: NotRequired["capo_backup_gateway.types.server_arn.ServerArn"]
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartVirtualMachinesMetadataSyncOutput) -> dict:
    out: dict = {}
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartVirtualMachinesMetadataSyncOutput:
    out: StartVirtualMachinesMetadataSyncOutput = {}  # type: ignore[typeddict-item]
    if "HypervisorArn" in data:
        out["hypervisor_arn"] = data["HypervisorArn"]
    return out
