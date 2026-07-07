"""Generated from Smithy shape ``com.amazonaws.storagegateway#SetSMBGuestPasswordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.smb_guest_password


class SetSMBGuestPasswordInput(TypedDict, closed=True):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The Amazon Resource Name (ARN) of the S3 File Gateway the SMB file share is associated with.</p>"""
    password: "aws_sdk_storage_gateway.types.smb_guest_password.SMBGuestPassword"
    """<p>The password that you want to set for your SMB server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetSMBGuestPasswordInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetSMBGuestPasswordInput:
    out: SetSMBGuestPasswordInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("SetSMBGuestPasswordInput.gateway_arn required")
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("SetSMBGuestPasswordInput.password required")
    return out
