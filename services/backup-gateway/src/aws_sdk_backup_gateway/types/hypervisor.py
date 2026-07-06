"""Generated from Smithy shape ``com.amazonaws.backupgateway#Hypervisor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.host
    import aws_sdk_backup_gateway.types.hypervisor_state
    import aws_sdk_backup_gateway.types.kms_key_arn
    import aws_sdk_backup_gateway.types.name
    import aws_sdk_backup_gateway.types.server_arn


class Hypervisor(TypedDict, closed=True):
    host: NotRequired["aws_sdk_backup_gateway.types.host.Host"]
    """<p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>"""
    hypervisor_arn: NotRequired["aws_sdk_backup_gateway.types.server_arn.ServerArn"]
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""
    kms_key_arn: NotRequired["aws_sdk_backup_gateway.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service used to encrypt the hypervisor.</p>"""
    name: NotRequired["aws_sdk_backup_gateway.types.name.Name"]
    """<p>The name of the hypervisor.</p>"""
    state: NotRequired["aws_sdk_backup_gateway.types.hypervisor_state.HypervisorState"]
    """<p>The state of the hypervisor.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Hypervisor) -> dict:
    out: dict = {}
    if "host" in value:
        out["Host"] = value["host"]
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Hypervisor:
    out: Hypervisor = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    if "HypervisorArn" in data:
        out["hypervisor_arn"] = data["HypervisorArn"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "State" in data:
        out["state"] = data["State"]
    return out
