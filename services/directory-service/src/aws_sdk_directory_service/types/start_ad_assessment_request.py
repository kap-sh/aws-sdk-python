"""Generated from Smithy shape ``com.amazonaws.directoryservice#StartADAssessmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_configuration
    import aws_sdk_directory_service.types.directory_id


class StartADAssessmentRequest(TypedDict):
    assessment_configuration: NotRequired[
        "aws_sdk_directory_service.types.assessment_configuration.AssessmentConfiguration"
    ]
    """<p>Configuration parameters for the directory assessment, including DNS server information, domain name, Amazon VPC subnet, and Amazon Web Services System Manager managed node details.</p>"""
    directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>The identifier of the directory for which to perform the assessment. This should be an existing directory. If the assessment is not for an existing directory, this parameter should be omitted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartADAssessmentRequest) -> dict:
    out: dict = {}
    if "assessment_configuration" in value:
        import aws_sdk_directory_service.types.assessment_configuration

        out["AssessmentConfiguration"] = (
            aws_sdk_directory_service.types.assessment_configuration.serialize_aws_json_1_1(
                value["assessment_configuration"]
            )
        )
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartADAssessmentRequest:
    out: StartADAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "AssessmentConfiguration" in data:
        import aws_sdk_directory_service.types.assessment_configuration

        out["assessment_configuration"] = (
            aws_sdk_directory_service.types.assessment_configuration.deserialize_aws_json_1_1(
                data["AssessmentConfiguration"]
            )
        )
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    return out
