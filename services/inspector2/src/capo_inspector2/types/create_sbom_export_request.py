"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateSbomExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.destination
    import capo_inspector2.types.resource_filter_criteria
    import capo_inspector2.types.sbom_report_format


class CreateSbomExportRequest(TypedDict, closed=True):
    resource_filter_criteria: NotRequired[
        "capo_inspector2.types.resource_filter_criteria.ResourceFilterCriteria"
    ]
    """<p>The resource filter criteria for the software bill of materials (SBOM) report.</p>"""
    report_format: "capo_inspector2.types.sbom_report_format.SbomReportFormat"
    """<p>The output format for the software bill of materials (SBOM) report.</p>"""
    s3_destination: "capo_inspector2.types.destination.Destination"
    """<p>Contains details of the Amazon S3 bucket and KMS key used to export findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSbomExportRequest) -> dict:
    out: dict = {}
    if "resource_filter_criteria" in value:
        import capo_inspector2.types.resource_filter_criteria

        out["resourceFilterCriteria"] = (
            capo_inspector2.types.resource_filter_criteria.serialize_json(
                value["resource_filter_criteria"]
            )
        )
    out["reportFormat"] = value["report_format"]
    import capo_inspector2.types.destination

    out["s3Destination"] = capo_inspector2.types.destination.serialize_json(
        value["s3_destination"]
    )
    return out


def deserialize_json(data: dict) -> CreateSbomExportRequest:
    out: CreateSbomExportRequest = {}  # type: ignore[typeddict-item]
    if "resourceFilterCriteria" in data:
        import capo_inspector2.types.resource_filter_criteria

        out["resource_filter_criteria"] = (
            capo_inspector2.types.resource_filter_criteria.deserialize_json(
                data["resourceFilterCriteria"]
            )
        )
    if "reportFormat" in data:
        out["report_format"] = data["reportFormat"]
    else:
        raise DeserializationError("CreateSbomExportRequest.report_format required")
    if "s3Destination" in data:
        import capo_inspector2.types.destination

        out["s3_destination"] = capo_inspector2.types.destination.deserialize_json(
            data["s3Destination"]
        )
    else:
        raise DeserializationError("CreateSbomExportRequest.s3_destination required")
    return out
