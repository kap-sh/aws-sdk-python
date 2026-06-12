"""Generated from Smithy shape ``com.amazonaws.storagegateway#JoinDomainOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.active_directory_status
    import aws_sdk_storage_gateway.types.gateway_arn


class JoinDomainOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    """<p>The unique Amazon Resource Name (ARN) of the gateway that joined the domain.</p>"""
    active_directory_status: NotRequired[
        "aws_sdk_storage_gateway.types.active_directory_status.ActiveDirectoryStatus"
    ]
    """<p>Indicates the status of the gateway as a member of the Active Directory domain.</p> <note> <p>This field is only used as part of a <code>JoinDomain</code> request. It is not affected by Active Directory connectivity changes that occur after the <code>JoinDomain</code> request succeeds.</p> </note> <ul> <li> <p> <code>ACCESS_DENIED</code>: Indicates that the <code>JoinDomain</code> operation failed due to an authentication error.</p> </li> <li> <p> <code>DETACHED</code>: Indicates that gateway is not joined to a domain.</p> </li> <li> <p> <code>JOINED</code>: Indicates that the gateway has successfully joined a domain.</p> </li> <li> <p> <code>JOINING</code>: Indicates that a <code>JoinDomain</code> operation is in progress.</p> </li> <li> <p> <code>INSUFFICIENT_PERMISSIONS</code>: Indicates that the <code>JoinDomain</code> operation failed because the specified user lacks the necessary permissions to join the domain.</p> </li> <li> <p> <code>NETWORK_ERROR</code>: Indicates that <code>JoinDomain</code> operation failed due to a network or connectivity error.</p> </li> <li> <p> <code>TIMEOUT</code>: Indicates that the <code>JoinDomain</code> operation failed because the operation didn't complete within the allotted time.</p> </li> <li> <p> <code>UNKNOWN_ERROR</code>: Indicates that the <code>JoinDomain</code> operation failed due to another type of error.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JoinDomainOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "active_directory_status" in value:
        import aws_sdk_storage_gateway.types.active_directory_status

        out["ActiveDirectoryStatus"] = (
            aws_sdk_storage_gateway.types.active_directory_status.serialize_aws_json_1_1(
                value["active_directory_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JoinDomainOutput:
    out: JoinDomainOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "ActiveDirectoryStatus" in data:
        import aws_sdk_storage_gateway.types.active_directory_status

        out["active_directory_status"] = (
            aws_sdk_storage_gateway.types.active_directory_status.deserialize_aws_json_1_1(
                data["ActiveDirectoryStatus"]
            )
        )
    return out
