"""Generated from Smithy shape ``com.amazonaws.auditmanager#ValidateAssessmentReportIntegrityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.s3_url


class ValidateAssessmentReportIntegrityRequest(TypedDict):
    s3_relative_path: "aws_sdk_auditmanager.types.s3_url.S3Url"
    """<p> The relative path of the Amazon S3 bucket that the assessment report is stored in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateAssessmentReportIntegrityRequest) -> dict:
    out: dict = {}
    out["s3RelativePath"] = value["s3_relative_path"]
    return out


def deserialize_json(data: dict) -> ValidateAssessmentReportIntegrityRequest:
    out: ValidateAssessmentReportIntegrityRequest = {}  # type: ignore[typeddict-item]
    if "s3RelativePath" in data:
        out["s3_relative_path"] = data["s3RelativePath"]
    else:
        raise DeserializationError(
            "ValidateAssessmentReportIntegrityRequest.s3_relative_path required"
        )
    return out
