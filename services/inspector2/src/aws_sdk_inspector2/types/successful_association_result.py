"""Generated from Smithy shape ``com.amazonaws.inspector2#SuccessfulAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_resource
    import aws_sdk_inspector2.types.scan_configuration_arn


class SuccessfulAssociationResult(TypedDict):
    scan_configuration_arn: NotRequired[
        "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the scan configuration that was successfully associated or disassociated.</p>"""
    resource: NotRequired[
        "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulAssociationResult) -> dict:
    out: dict = {}
    if "scan_configuration_arn" in value:
        out["scanConfigurationArn"] = value["scan_configuration_arn"]
    if "resource" in value:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.serialize_json(
                value["resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> SuccessfulAssociationResult:
    out: SuccessfulAssociationResult = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    if "resource" in data:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.deserialize_json(
                data["resource"]
            )
        )
    return out
