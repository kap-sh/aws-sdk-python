"""Generated from Smithy shape ``com.amazonaws.backupgateway#UpdateHypervisorInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.host
    import aws_sdk_backup_gateway.types.log_group_arn
    import aws_sdk_backup_gateway.types.name
    import aws_sdk_backup_gateway.types.password
    import aws_sdk_backup_gateway.types.server_arn
    import aws_sdk_backup_gateway.types.username


class UpdateHypervisorInput(TypedDict):
    hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn"
    """<p>The Amazon Resource Name (ARN) of the hypervisor to update.</p>"""
    host: NotRequired["aws_sdk_backup_gateway.types.host.Host"]
    """<p>The updated host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>"""
    username: NotRequired["aws_sdk_backup_gateway.types.username.Username"]
    """<p>The updated username for the hypervisor.</p>"""
    password: NotRequired["aws_sdk_backup_gateway.types.password.Password"]
    """<p>The updated password for the hypervisor.</p>"""
    name: NotRequired["aws_sdk_backup_gateway.types.name.Name"]
    """<p>The updated name for the hypervisor</p>"""
    log_group_arn: NotRequired["aws_sdk_backup_gateway.types.log_group_arn.LogGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the group of gateways within the requested log.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateHypervisorInput) -> dict:
    out: dict = {}
    out["HypervisorArn"] = value["hypervisor_arn"]
    if "host" in value:
        out["Host"] = value["host"]
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    if "name" in value:
        out["Name"] = value["name"]
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateHypervisorInput:
    out: UpdateHypervisorInput = {}  # type: ignore[typeddict-item]
    if "HypervisorArn" in data:
        out["hypervisor_arn"] = data["HypervisorArn"]
    else:
        raise DeserializationError("UpdateHypervisorInput.hypervisor_arn required")
    if "Host" in data:
        out["host"] = data["Host"]
    if "Username" in data:
        out["username"] = data["Username"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    return out
