"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#GetReportDefinitionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_applicationcostprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.format
    import aws_sdk_applicationcostprofiler.types.report_description
    import aws_sdk_applicationcostprofiler.types.report_frequency
    import aws_sdk_applicationcostprofiler.types.report_id
    import aws_sdk_applicationcostprofiler.types.s3_location
    import aws_sdk_applicationcostprofiler.types.timestamp


class GetReportDefinitionResult(TypedDict, closed=True):
    report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId"
    """<p>ID of the report retrieved.</p>"""
    report_description: (
        "aws_sdk_applicationcostprofiler.types.report_description.ReportDescription"
    )
    """<p>Description of the report.</p>"""
    report_frequency: (
        "aws_sdk_applicationcostprofiler.types.report_frequency.ReportFrequency"
    )
    """<p>Cadence used to generate the report.</p>"""
    format: "aws_sdk_applicationcostprofiler.types.format.Format"
    """<p>Format of the generated report.</p>"""
    destination_s3_location: (
        "aws_sdk_applicationcostprofiler.types.s3_location.S3Location"
    )
    """<p>Amazon Simple Storage Service (Amazon S3) location where the report is uploaded.</p>"""
    created_at: "aws_sdk_applicationcostprofiler.types.timestamp.Timestamp"
    """<p>Timestamp (milliseconds) when this report definition was created.</p>"""
    last_updated: "aws_sdk_applicationcostprofiler.types.timestamp.Timestamp"
    """<p>Timestamp (milliseconds) when this report definition was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReportDefinitionResult) -> dict:
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
    import aws_sdk_applicationcostprofiler.types.timestamp

    out["createdAt"] = aws_sdk_applicationcostprofiler.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_applicationcostprofiler.types.timestamp

    out["lastUpdated"] = aws_sdk_applicationcostprofiler.types.timestamp.serialize_json(
        value["last_updated"]
    )
    return out


def deserialize_json(data: dict) -> GetReportDefinitionResult:
    out: GetReportDefinitionResult = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    else:
        raise DeserializationError("GetReportDefinitionResult.report_id required")
    if "reportDescription" in data:
        out["report_description"] = data["reportDescription"]
    else:
        raise DeserializationError(
            "GetReportDefinitionResult.report_description required"
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
            "GetReportDefinitionResult.report_frequency required"
        )
    if "format" in data:
        import aws_sdk_applicationcostprofiler.types.format

        out["format"] = aws_sdk_applicationcostprofiler.types.format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("GetReportDefinitionResult.format required")
    if "destinationS3Location" in data:
        import aws_sdk_applicationcostprofiler.types.s3_location

        out["destination_s3_location"] = (
            aws_sdk_applicationcostprofiler.types.s3_location.deserialize_json(
                data["destinationS3Location"]
            )
        )
    else:
        raise DeserializationError(
            "GetReportDefinitionResult.destination_s3_location required"
        )
    if "createdAt" in data:
        import aws_sdk_applicationcostprofiler.types.timestamp

        out["created_at"] = (
            aws_sdk_applicationcostprofiler.types.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetReportDefinitionResult.created_at required")
    if "lastUpdated" in data:
        import aws_sdk_applicationcostprofiler.types.timestamp

        out["last_updated"] = (
            aws_sdk_applicationcostprofiler.types.timestamp.deserialize_json(
                data["lastUpdated"]
            )
        )
    else:
        raise DeserializationError("GetReportDefinitionResult.last_updated required")
    return out
