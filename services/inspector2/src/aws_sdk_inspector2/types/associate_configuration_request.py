"""Generated from Smithy shape ``com.amazonaws.inspector2#AssociateConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_resource
    import aws_sdk_inspector2.types.scan_configuration_arn


class AssociateConfigurationRequest(TypedDict):
    scan_configuration_arn: (
        "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the scan configuration.</p>"""
    resource: "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource"


# --- restJson1 ser/de ---
def serialize_json(value: AssociateConfigurationRequest) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    import aws_sdk_inspector2.types.code_security_resource

    out["resource"] = aws_sdk_inspector2.types.code_security_resource.serialize_json(
        value["resource"]
    )
    return out


def deserialize_json(data: dict) -> AssociateConfigurationRequest:
    out: AssociateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError(
            "AssociateConfigurationRequest.scan_configuration_arn required"
        )
    if "resource" in data:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.deserialize_json(
                data["resource"]
            )
        )
    else:
        raise DeserializationError("AssociateConfigurationRequest.resource required")
    return out
