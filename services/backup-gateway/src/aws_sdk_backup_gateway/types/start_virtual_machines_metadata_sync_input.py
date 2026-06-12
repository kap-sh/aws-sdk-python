"""Generated from Smithy shape ``com.amazonaws.backupgateway#StartVirtualMachinesMetadataSyncInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.server_arn


class StartVirtualMachinesMetadataSyncInput(TypedDict):
    hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn"
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartVirtualMachinesMetadataSyncInput) -> dict:
    out: dict = {}
    out["HypervisorArn"] = value["hypervisor_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartVirtualMachinesMetadataSyncInput:
    out: StartVirtualMachinesMetadataSyncInput = {}  # type: ignore[typeddict-item]
    if "HypervisorArn" in data:
        out["hypervisor_arn"] = data["HypervisorArn"]
    else:
        raise DeserializationError(
            "StartVirtualMachinesMetadataSyncInput.hypervisor_arn required"
        )
    return out
