"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetDICOMImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.dicom_import_job_properties


class GetDICOMImportJobResponse(TypedDict):
    job_properties: "aws_sdk_medical_imaging.types.dicom_import_job_properties.DICOMImportJobProperties"
    """<p>The properties of the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDICOMImportJobResponse) -> dict:
    out: dict = {}
    import aws_sdk_medical_imaging.types.dicom_import_job_properties

    out["jobProperties"] = (
        aws_sdk_medical_imaging.types.dicom_import_job_properties.serialize_json(
            value["job_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDICOMImportJobResponse:
    out: GetDICOMImportJobResponse = {}  # type: ignore[typeddict-item]
    if "jobProperties" in data:
        import aws_sdk_medical_imaging.types.dicom_import_job_properties

        out["job_properties"] = (
            aws_sdk_medical_imaging.types.dicom_import_job_properties.deserialize_json(
                data["jobProperties"]
            )
        )
    else:
        raise DeserializationError("GetDICOMImportJobResponse.job_properties required")
    return out
