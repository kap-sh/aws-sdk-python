"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ReportDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.format
    import aws_sdk_applicationcostprofiler.types.report_description
    import aws_sdk_applicationcostprofiler.types.report_frequency
    import aws_sdk_applicationcostprofiler.types.report_id
    import aws_sdk_applicationcostprofiler.types.s3_location
    import aws_sdk_applicationcostprofiler.types.timestamp


class ReportDefinition(TypedDict, closed=True):
    report_id: NotRequired["aws_sdk_applicationcostprofiler.types.report_id.ReportId"]
    """<p>The ID of the report.</p>"""
    report_description: NotRequired[
        "aws_sdk_applicationcostprofiler.types.report_description.ReportDescription"
    ]
    """<p>Description of the report</p>"""
    report_frequency: NotRequired[
        "aws_sdk_applicationcostprofiler.types.report_frequency.ReportFrequency"
    ]
    """<p>The cadence at which the report is generated.</p>"""
    format: NotRequired["aws_sdk_applicationcostprofiler.types.format.Format"]
    """<p>The format used for the generated reports.</p>"""
    destination_s3_location: NotRequired[
        "aws_sdk_applicationcostprofiler.types.s3_location.S3Location"
    ]
    """<p>The location in Amazon Simple Storage Service (Amazon S3) the reports should be saved to.</p>"""
    created_at: NotRequired["aws_sdk_applicationcostprofiler.types.timestamp.Timestamp"]
    """<p>Timestamp (milliseconds) when this report definition was created.</p>"""
    last_updated_at: NotRequired[
        "aws_sdk_applicationcostprofiler.types.timestamp.Timestamp"
    ]
    """<p>Timestamp (milliseconds) when this report definition was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportDefinition) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    if "report_description" in value:
        out["reportDescription"] = value["report_description"]
    if "report_frequency" in value:
        import aws_sdk_applicationcostprofiler.types.report_frequency

        out["reportFrequency"] = (
            aws_sdk_applicationcostprofiler.types.report_frequency.serialize_json(
                value["report_frequency"]
            )
        )
    if "format" in value:
        import aws_sdk_applicationcostprofiler.types.format

        out["format"] = aws_sdk_applicationcostprofiler.types.format.serialize_json(
            value["format"]
        )
    if "destination_s3_location" in value:
        import aws_sdk_applicationcostprofiler.types.s3_location

        out["destinationS3Location"] = (
            aws_sdk_applicationcostprofiler.types.s3_location.serialize_json(
                value["destination_s3_location"]
            )
        )
    if "created_at" in value:
        import aws_sdk_applicationcostprofiler.types.timestamp

        out["createdAt"] = (
            aws_sdk_applicationcostprofiler.types.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_applicationcostprofiler.types.timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_applicationcostprofiler.types.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReportDefinition:
    out: ReportDefinition = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    if "reportDescription" in data:
        out["report_description"] = data["reportDescription"]
    if "reportFrequency" in data:
        import aws_sdk_applicationcostprofiler.types.report_frequency

        out["report_frequency"] = (
            aws_sdk_applicationcostprofiler.types.report_frequency.deserialize_json(
                data["reportFrequency"]
            )
        )
    if "format" in data:
        import aws_sdk_applicationcostprofiler.types.format

        out["format"] = aws_sdk_applicationcostprofiler.types.format.deserialize_json(
            data["format"]
        )
    if "destinationS3Location" in data:
        import aws_sdk_applicationcostprofiler.types.s3_location

        out["destination_s3_location"] = (
            aws_sdk_applicationcostprofiler.types.s3_location.deserialize_json(
                data["destinationS3Location"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_applicationcostprofiler.types.timestamp

        out["created_at"] = (
            aws_sdk_applicationcostprofiler.types.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_applicationcostprofiler.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_applicationcostprofiler.types.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
