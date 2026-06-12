"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportsDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_report_destination_type
    import aws_sdk_auditmanager.types.s3_url


class AssessmentReportsDestination(TypedDict):
    destination_type: NotRequired[
        "aws_sdk_auditmanager.types.assessment_report_destination_type.AssessmentReportDestinationType"
    ]
    """<p> The destination type, such as Amazon S3. </p>"""
    destination: NotRequired["aws_sdk_auditmanager.types.s3_url.S3Url"]
    """<p> The destination bucket where Audit Manager stores assessment reports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportsDestination) -> dict:
    out: dict = {}
    if "destination_type" in value:
        import aws_sdk_auditmanager.types.assessment_report_destination_type

        out["destinationType"] = (
            aws_sdk_auditmanager.types.assessment_report_destination_type.serialize_json(
                value["destination_type"]
            )
        )
    if "destination" in value:
        out["destination"] = value["destination"]
    return out


def deserialize_json(data: dict) -> AssessmentReportsDestination:
    out: AssessmentReportsDestination = {}  # type: ignore[typeddict-item]
    if "destinationType" in data:
        import aws_sdk_auditmanager.types.assessment_report_destination_type

        out["destination_type"] = (
            aws_sdk_auditmanager.types.assessment_report_destination_type.deserialize_json(
                data["destinationType"]
            )
        )
    if "destination" in data:
        out["destination"] = data["destination"]
    return out
