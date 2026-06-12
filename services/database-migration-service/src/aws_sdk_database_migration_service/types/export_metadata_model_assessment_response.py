"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ExportMetadataModelAssessmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry


class ExportMetadataModelAssessmentResponse(TypedDict):
    pdf_report: NotRequired[
        "aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry.ExportMetadataModelAssessmentResultEntry"
    ]
    """<p>The Amazon S3 details for an assessment exported in PDF format.</p>"""
    csv_report: NotRequired[
        "aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry.ExportMetadataModelAssessmentResultEntry"
    ]
    """<p>The Amazon S3 details for an assessment exported in CSV format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportMetadataModelAssessmentResponse) -> dict:
    out: dict = {}
    if "pdf_report" in value:
        import aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry

        out["PdfReport"] = (
            aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry.serialize_aws_json_1_1(
                value["pdf_report"]
            )
        )
    if "csv_report" in value:
        import aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry

        out["CsvReport"] = (
            aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry.serialize_aws_json_1_1(
                value["csv_report"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportMetadataModelAssessmentResponse:
    out: ExportMetadataModelAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "PdfReport" in data:
        import aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry

        out["pdf_report"] = (
            aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry.deserialize_aws_json_1_1(
                data["PdfReport"]
            )
        )
    if "CsvReport" in data:
        import aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry

        out["csv_report"] = (
            aws_sdk_database_migration_service.types.export_metadata_model_assessment_result_entry.deserialize_aws_json_1_1(
                data["CsvReport"]
            )
        )
    return out
