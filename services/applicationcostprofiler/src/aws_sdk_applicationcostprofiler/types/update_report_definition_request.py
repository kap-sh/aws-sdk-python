"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#UpdateReportDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_applicationcostprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.format
    import aws_sdk_applicationcostprofiler.types.report_description
    import aws_sdk_applicationcostprofiler.types.report_frequency
    import aws_sdk_applicationcostprofiler.types.report_id
    import aws_sdk_applicationcostprofiler.types.s3_location


class UpdateReportDefinitionRequest(TypedDict):
    report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId"
    """<p>Required. ID of the report to update.</p>"""
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
def serialize_json(value: UpdateReportDefinitionRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> UpdateReportDefinitionRequest:
    out: UpdateReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "reportDescription" in data:
        out["report_description"] = data["reportDescription"]
    else:
        raise DeserializationError(
            "UpdateReportDefinitionRequest.report_description required"
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
            "UpdateReportDefinitionRequest.report_frequency required"
        )
    if "format" in data:
        import aws_sdk_applicationcostprofiler.types.format

        out["format"] = aws_sdk_applicationcostprofiler.types.format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("UpdateReportDefinitionRequest.format required")
    if "destinationS3Location" in data:
        import aws_sdk_applicationcostprofiler.types.s3_location

        out["destination_s3_location"] = (
            aws_sdk_applicationcostprofiler.types.s3_location.deserialize_json(
                data["destinationS3Location"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateReportDefinitionRequest.destination_s3_location required"
        )
    return out
