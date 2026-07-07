"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#PutReportDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_applicationcostprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.format
    import aws_sdk_applicationcostprofiler.types.report_description
    import aws_sdk_applicationcostprofiler.types.report_frequency
    import aws_sdk_applicationcostprofiler.types.report_id
    import aws_sdk_applicationcostprofiler.types.s3_location


class PutReportDefinitionRequest(TypedDict, closed=True):
    report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId"
    """<p>Required. ID of the report. You can choose any valid string matching the pattern for the ID.</p>"""
    report_description: (
        "aws_sdk_applicationcostprofiler.types.report_description.ReportDescription"
    )
    """<p>Required. Description of the report.</p>"""
    report_frequency: (
        "aws_sdk_applicationcostprofiler.types.report_frequency.ReportFrequency"
    )
    """<p>Required. The cadence to generate the report.</p>"""
    format: "aws_sdk_applicationcostprofiler.types.format.Format"
    """<p>Required. The format to use for the generated report.</p>"""
    destination_s3_location: (
        "aws_sdk_applicationcostprofiler.types.s3_location.S3Location"
    )
    """<p>Required. Amazon Simple Storage Service (Amazon S3) location where Application Cost Profiler uploads the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutReportDefinitionRequest) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    out["reportDescription"] = value["report_description"]
    import aws_sdk_applicationcostprofiler.types.report_frequency

    out["reportFrequency"] = (
        aws_sdk_applicationcostprofiler.types.report_frequency.serialize_json(
            value["report_frequency"]
        )
    )
    import aws_sdk_applicationcostprofiler.types.format

    out["format"] = aws_sdk_applicationcostprofiler.types.format.serialize_json(
        value["format"]
    )
    import aws_sdk_applicationcostprofiler.types.s3_location

    out["destinationS3Location"] = (
        aws_sdk_applicationcostprofiler.types.s3_location.serialize_json(
            value["destination_s3_location"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutReportDefinitionRequest:
    out: PutReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    else:
        raise DeserializationError("PutReportDefinitionRequest.report_id required")
    if "reportDescription" in data:
        out["report_description"] = data["reportDescription"]
    else:
        raise DeserializationError(
            "PutReportDefinitionRequest.report_description required"
        )
    if "reportFrequency" in data:
        import aws_sdk_applicationcostprofiler.types.report_frequency

        out["report_frequency"] = (
            aws_sdk_applicationcostprofiler.types.report_frequency.deserialize_json(
                data["reportFrequency"]
            )
        )
    else:
        raise DeserializationError(
            "PutReportDefinitionRequest.report_frequency required"
        )
    if "format" in data:
        import aws_sdk_applicationcostprofiler.types.format

        out["format"] = aws_sdk_applicationcostprofiler.types.format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("PutReportDefinitionRequest.format required")
    if "destinationS3Location" in data:
        import aws_sdk_applicationcostprofiler.types.s3_location

        out["destination_s3_location"] = (
            aws_sdk_applicationcostprofiler.types.s3_location.deserialize_json(
                data["destinationS3Location"]
            )
        )
    else:
        raise DeserializationError(
            "PutReportDefinitionRequest.destination_s3_location required"
        )
    return out
