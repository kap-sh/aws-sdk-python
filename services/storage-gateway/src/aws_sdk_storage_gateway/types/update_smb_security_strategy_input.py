"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateSMBSecurityStrategyInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.smb_security_strategy


class UpdateSMBSecurityStrategyInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    smb_security_strategy: (
        "aws_sdk_storage_gateway.types.smb_security_strategy.SMBSecurityStrategy"
    )
    """<p>Specifies the type of security strategy.</p> <p> <code>ClientSpecified</code>: If you choose this option, requests are established based on what is negotiated by the client. This option is recommended when you want to maximize compatibility across different clients in your environment. Supported only for S3 File Gateway.</p> <p> <code>MandatorySigning</code>: If you choose this option, File Gateway only allows connections from SMBv2 or SMBv3 clients that have signing enabled. This option works with SMB clients on Microsoft Windows Vista, Windows Server 2008 or newer.</p> <p> <code>MandatoryEncryption</code>: If you choose this option, File Gateway only allows connections from SMBv3 clients that have encryption enabled. This option is recommended for environments that handle sensitive data. This option works with SMB clients on Microsoft Windows 8, Windows Server 2012 or newer.</p> <p> <code>MandatoryEncryptionNoAes128</code>: If you choose this option, File Gateway only allows connections from SMBv3 clients that use 256-bit AES encryption algorithms. 128-bit algorithms are not allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSMBSecurityStrategyInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    import aws_sdk_storage_gateway.types.smb_security_strategy

    out["SMBSecurityStrategy"] = (
        aws_sdk_storage_gateway.types.smb_security_strategy.serialize_aws_json_1_1(
            value["smb_security_strategy"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSMBSecurityStrategyInput:
    out: UpdateSMBSecurityStrategyInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError(
            "UpdateSMBSecurityStrategyInput.gateway_arn required"
        )
    if "SMBSecurityStrategy" in data:
        import aws_sdk_storage_gateway.types.smb_security_strategy

        out["smb_security_strategy"] = (
            aws_sdk_storage_gateway.types.smb_security_strategy.deserialize_aws_json_1_1(
                data["SMBSecurityStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSMBSecurityStrategyInput.smb_security_strategy required"
        )
    return out
