"""Generated from Smithy shape ``com.amazonaws.inspector2#DisassociateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_resource
    import aws_sdk_inspector2.types.scan_configuration_arn


class DisassociateConfigurationRequest(TypedDict, closed=True):
    scan_configuration_arn: (
        "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the scan configuration to disassociate from a code repository.</p>"""
    resource: "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource"


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateConfigurationRequest) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    import aws_sdk_inspector2.types.code_security_resource

    out["resource"] = aws_sdk_inspector2.types.code_security_resource.serialize_json(
        value["resource"]
    )
    return out


def deserialize_json(data: dict) -> DisassociateConfigurationRequest:
    out: DisassociateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError(
            "DisassociateConfigurationRequest.scan_configuration_arn required"
        )
    if "resource" in data:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.deserialize_json(
                data["resource"]
            )
        )
    else:
        raise DeserializationError("DisassociateConfigurationRequest.resource required")
    return out
