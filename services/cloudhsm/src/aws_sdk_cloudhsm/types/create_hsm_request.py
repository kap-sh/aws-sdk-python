"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CreateHsmRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.client_token
    import aws_sdk_cloudhsm.types.external_id
    import aws_sdk_cloudhsm.types.iam_role_arn
    import aws_sdk_cloudhsm.types.ip_address
    import aws_sdk_cloudhsm.types.ssh_key
    import aws_sdk_cloudhsm.types.subnet_id
    import aws_sdk_cloudhsm.types.subscription_type


class CreateHsmRequest(TypedDict):
    subnet_id: "aws_sdk_cloudhsm.types.subnet_id.SubnetId"
    """<p>The identifier of the subnet in your VPC in which to place the HSM.</p>"""
    ssh_key: "aws_sdk_cloudhsm.types.ssh_key.SshKey"
    """<p>The SSH public key to install on the HSM.</p>"""
    eni_ip: NotRequired["aws_sdk_cloudhsm.types.ip_address.IpAddress"]
    """<p>The IP address to assign to the HSM's ENI.</p> <p>If an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the subnet.</p>"""
    iam_role_arn: "aws_sdk_cloudhsm.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of an IAM role to enable the AWS CloudHSM service to allocate an ENI on your behalf.</p>"""
    external_id: NotRequired["aws_sdk_cloudhsm.types.external_id.ExternalId"]
    """<p>The external ID from <code>IamRoleArn</code>, if present.</p>"""
    subscription_type: "aws_sdk_cloudhsm.types.subscription_type.SubscriptionType"
    client_token: NotRequired["aws_sdk_cloudhsm.types.client_token.ClientToken"]
    """<p>A user-defined token to ensure idempotence. Subsequent calls to this operation with the same token will be ignored.</p>"""
    syslog_ip: NotRequired["aws_sdk_cloudhsm.types.ip_address.IpAddress"]
    """<p>The IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHsmRequest) -> dict:
    out: dict = {}
    out["SubnetId"] = value["subnet_id"]
    out["SshKey"] = value["ssh_key"]
    if "eni_ip" in value:
        out["EniIp"] = value["eni_ip"]
    out["IamRoleArn"] = value["iam_role_arn"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    import aws_sdk_cloudhsm.types.subscription_type

    out["SubscriptionType"] = (
        aws_sdk_cloudhsm.types.subscription_type.serialize_aws_json_1_1(
            value["subscription_type"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "syslog_ip" in value:
        out["SyslogIp"] = value["syslog_ip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHsmRequest:
    out: CreateHsmRequest = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    else:
        raise DeserializationError("CreateHsmRequest.subnet_id required")
    if "SshKey" in data:
        out["ssh_key"] = data["SshKey"]
    else:
        raise DeserializationError("CreateHsmRequest.ssh_key required")
    if "EniIp" in data:
        out["eni_ip"] = data["EniIp"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("CreateHsmRequest.iam_role_arn required")
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    if "SubscriptionType" in data:
        import aws_sdk_cloudhsm.types.subscription_type

        out["subscription_type"] = (
            aws_sdk_cloudhsm.types.subscription_type.deserialize_aws_json_1_1(
                data["SubscriptionType"]
            )
        )
    else:
        raise DeserializationError("CreateHsmRequest.subscription_type required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "SyslogIp" in data:
        out["syslog_ip"] = data["SyslogIp"]
    return out
