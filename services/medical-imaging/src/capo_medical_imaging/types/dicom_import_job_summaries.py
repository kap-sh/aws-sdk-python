"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMImportJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_import_job_summary

DICOMImportJobSummaries: TypeAlias = list[
    "capo_medical_imaging.types.dicom_import_job_summary.DICOMImportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DICOMImportJobSummaries) -> list:
    import capo_medical_imaging.types.dicom_import_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_medical_imaging.types.dicom_import_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DICOMImportJobSummaries:
    import capo_medical_imaging.types.dicom_import_job_summary

    out: DICOMImportJobSummaries = []
    for item in data:
        out.append(
            capo_medical_imaging.types.dicom_import_job_summary.deserialize_json(item)
        )
    return out
