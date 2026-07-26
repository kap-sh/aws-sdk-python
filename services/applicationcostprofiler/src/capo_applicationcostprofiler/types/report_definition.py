"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ReportDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.format
    import capo_applicationcostprofiler.types.report_description
    import capo_applicationcostprofiler.types.report_frequency
    import capo_applicationcostprofiler.types.report_id
    import capo_applicationcostprofiler.types.s3_location
    import capo_applicationcostprofiler.types.timestamp


class ReportDefinition(TypedDict, closed=True):
    report_id: NotRequired["capo_applicationcostprofiler.types.report_id.ReportId"]
    """<p>The ID of the report.</p>"""
    report_description: NotRequired[
        "capo_applicationcostprofiler.types.report_description.ReportDescription"
    ]
    """<p>Description of the report</p>"""
    report_frequency: NotRequired[
        "capo_applicationcostprofiler.types.report_frequency.ReportFrequency"
    ]
    """<p>The cadence at which the report is generated.</p>"""
    format: NotRequired["capo_applicationcostprofiler.types.format.Format"]
    """<p>The format used for the generated reports.</p>"""
    destination_s3_location: NotRequired[
        "capo_applicationcostprofiler.types.s3_location.S3Location"
    ]
    """<p>The location in Amazon Simple Storage Service (Amazon S3) the reports should be saved to.</p>"""
    created_at: NotRequired["capo_applicationcostprofiler.types.timestamp.Timestamp"]
    """<p>Timestamp (milliseconds) when this report definition was created.</p>"""
    last_updated_at: NotRequired[
        "capo_applicationcostprofiler.types.timestamp.Timestamp"
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
        import capo_applicationcostprofiler.types.report_frequency

        out["reportFrequency"] = (
            capo_applicationcostprofiler.types.report_frequency.serialize_json(
                value["report_frequency"]
            )
        )
    if "format" in value:
        import capo_applicationcostprofiler.types.format

        out["format"] = capo_applicationcostprofiler.types.format.serialize_json(
            value["format"]
        )
    if "destination_s3_location" in value:
        import capo_applicationcostprofiler.types.s3_location

        out["destinationS3Location"] = (
            capo_applicationcostprofiler.types.s3_location.serialize_json(
                value["destination_s3_location"]
            )
        )
    if "created_at" in value:
        import capo_applicationcostprofiler.types.timestamp

        out["createdAt"] = capo_applicationcostprofiler.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_applicationcostprofiler.types.timestamp

        out["lastUpdatedAt"] = (
            capo_applicationcostprofiler.types.timestamp.serialize_json(
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
        import capo_applicationcostprofiler.types.report_frequency

        out["report_frequency"] = (
            capo_applicationcostprofiler.types.report_frequency.deserialize_json(
                data["reportFrequency"]
            )
        )
    if "format" in data:
        import capo_applicationcostprofiler.types.format

        out["format"] = capo_applicationcostprofiler.types.format.deserialize_json(
            data["format"]
        )
    if "destinationS3Location" in data:
        import capo_applicationcostprofiler.types.s3_location

        out["destination_s3_location"] = (
            capo_applicationcostprofiler.types.s3_location.deserialize_json(
                data["destinationS3Location"]
            )
        )
    if "createdAt" in data:
        import capo_applicationcostprofiler.types.timestamp

        out["created_at"] = (
            capo_applicationcostprofiler.types.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import capo_applicationcostprofiler.types.timestamp

        out["last_updated_at"] = (
            capo_applicationcostprofiler.types.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
