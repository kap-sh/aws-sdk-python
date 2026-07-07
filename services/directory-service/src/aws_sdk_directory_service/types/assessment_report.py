"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_validations
    import aws_sdk_directory_service.types.ip_addr


class AssessmentReport(TypedDict, closed=True):
    domain_controller_ip: NotRequired["aws_sdk_directory_service.types.ip_addr.IpAddr"]
    """<p>The IP address of the domain controller that was tested during the assessment.</p>"""
    validations: NotRequired[
        "aws_sdk_directory_service.types.assessment_validations.AssessmentValidations"
    ]
    """<p>A list of validation results for different test categories performed against this domain controller.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentReport) -> dict:
    out: dict = {}
    if "domain_controller_ip" in value:
        out["DomainControllerIp"] = value["domain_controller_ip"]
    if "validations" in value:
        import aws_sdk_directory_service.types.assessment_validations

        out["Validations"] = (
            aws_sdk_directory_service.types.assessment_validations.serialize_aws_json_1_1(
                value["validations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentReport:
    out: AssessmentReport = {}  # type: ignore[typeddict-item]
    if "DomainControllerIp" in data:
        out["domain_controller_ip"] = data["DomainControllerIp"]
    if "Validations" in data:
        import aws_sdk_directory_service.types.assessment_validations

        out["validations"] = (
            aws_sdk_directory_service.types.assessment_validations.deserialize_aws_json_1_1(
                data["Validations"]
            )
        )
    return out
