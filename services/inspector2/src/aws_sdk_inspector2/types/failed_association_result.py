"""Generated from Smithy shape ``com.amazonaws.inspector2#FailedAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.association_result_status_code
    import aws_sdk_inspector2.types.association_result_status_message
    import aws_sdk_inspector2.types.code_security_resource
    import aws_sdk_inspector2.types.scan_configuration_arn


class FailedAssociationResult(TypedDict):
    scan_configuration_arn: NotRequired[
        "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the scan configuration that failed to be associated or disassociated.</p>"""
    resource: NotRequired[
        "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource"
    ]
    status_code: NotRequired[
        "aws_sdk_inspector2.types.association_result_status_code.AssociationResultStatusCode"
    ]
    """<p>The status code indicating why the association or disassociation failed.</p>"""
    status_message: NotRequired[
        "aws_sdk_inspector2.types.association_result_status_message.AssociationResultStatusMessage"
    ]
    """<p>A message explaining why the association or disassociation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedAssociationResult) -> dict:
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
    if "status_code" in value:
        import aws_sdk_inspector2.types.association_result_status_code

        out["statusCode"] = (
            aws_sdk_inspector2.types.association_result_status_code.serialize_json(
                value["status_code"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> FailedAssociationResult:
    out: FailedAssociationResult = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    if "resource" in data:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.deserialize_json(
                data["resource"]
            )
        )
    if "statusCode" in data:
        import aws_sdk_inspector2.types.association_result_status_code

        out["status_code"] = (
            aws_sdk_inspector2.types.association_result_status_code.deserialize_json(
                data["statusCode"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
