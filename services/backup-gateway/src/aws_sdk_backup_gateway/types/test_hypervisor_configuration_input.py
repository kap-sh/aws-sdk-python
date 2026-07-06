"""Generated from Smithy shape ``com.amazonaws.backupgateway#TestHypervisorConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway_arn
    import aws_sdk_backup_gateway.types.host
    import aws_sdk_backup_gateway.types.password
    import aws_sdk_backup_gateway.types.username


class TestHypervisorConfigurationInput(TypedDict, closed=True):
    gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway to the hypervisor to test.</p>"""
    host: "aws_sdk_backup_gateway.types.host.Host"
    """<p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>"""
    username: NotRequired["aws_sdk_backup_gateway.types.username.Username"]
    """<p>The username for the hypervisor.</p>"""
    password: NotRequired["aws_sdk_backup_gateway.types.password.Password"]
    """<p>The password for the hypervisor.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestHypervisorConfigurationInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    out["Host"] = value["host"]
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TestHypervisorConfigurationInput:
    out: TestHypervisorConfigurationInput = {}  # type: ignore[typeddict-item]
    if "GatewayArn" in data:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        raise DeserializationError(
            "TestHypervisorConfigurationInput.gateway_arn required"
        )
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("TestHypervisorConfigurationInput.host required")
    if "Username" in data:
        out["username"] = data["Username"]
    if "Password" in data:
        out["password"] = data["Password"]
    return out
