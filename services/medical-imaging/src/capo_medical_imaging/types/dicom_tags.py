"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMTags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_accession_number
    import capo_medical_imaging.types.dicom_number_of_study_related_instances
    import capo_medical_imaging.types.dicom_number_of_study_related_series
    import capo_medical_imaging.types.dicom_patient_birth_date
    import capo_medical_imaging.types.dicom_patient_id
    import capo_medical_imaging.types.dicom_patient_name
    import capo_medical_imaging.types.dicom_patient_sex
    import capo_medical_imaging.types.dicom_series_body_part
    import capo_medical_imaging.types.dicom_series_instance_uid
    import capo_medical_imaging.types.dicom_series_modality
    import capo_medical_imaging.types.dicom_series_number
    import capo_medical_imaging.types.dicom_study_date
    import capo_medical_imaging.types.dicom_study_description
    import capo_medical_imaging.types.dicom_study_id
    import capo_medical_imaging.types.dicom_study_instance_uid
    import capo_medical_imaging.types.dicom_study_time


class DICOMTags(TypedDict, closed=True):
    dicom_patient_id: NotRequired[
        "capo_medical_imaging.types.dicom_patient_id.DICOMPatientId"
    ]
    """<p>The unique identifier for a patient in a DICOM Study.</p>"""
    dicom_patient_name: NotRequired[
        "capo_medical_imaging.types.dicom_patient_name.DICOMPatientName"
    ]
    """<p>The patient name.</p>"""
    dicom_patient_birth_date: NotRequired[
        "capo_medical_imaging.types.dicom_patient_birth_date.DICOMPatientBirthDate"
    ]
    """<p>The patient birth date.</p>"""
    dicom_patient_sex: NotRequired[
        "capo_medical_imaging.types.dicom_patient_sex.DICOMPatientSex"
    ]
    """<p>The patient sex.</p>"""
    dicom_study_instance_uid: NotRequired[
        "capo_medical_imaging.types.dicom_study_instance_uid.DICOMStudyInstanceUID"
    ]
    """<p>The DICOM provided identifier for the Study Instance UID.</p>"""
    dicom_study_id: NotRequired[
        "capo_medical_imaging.types.dicom_study_id.DICOMStudyId"
    ]
    """<p>The DICOM provided identifier for the Study ID.</p>"""
    dicom_study_description: NotRequired[
        "capo_medical_imaging.types.dicom_study_description.DICOMStudyDescription"
    ]
    """<p>The DICOM provided Study Description.</p>"""
    dicom_number_of_study_related_series: "capo_medical_imaging.types.dicom_number_of_study_related_series.DICOMNumberOfStudyRelatedSeries"
    """<p>The total number of series in the DICOM study.</p>"""
    dicom_number_of_study_related_instances: "capo_medical_imaging.types.dicom_number_of_study_related_instances.DICOMNumberOfStudyRelatedInstances"
    """<p>The total number of instances in the DICOM study.</p>"""
    dicom_accession_number: NotRequired[
        "capo_medical_imaging.types.dicom_accession_number.DICOMAccessionNumber"
    ]
    """<p>The accession number for the DICOM study.</p>"""
    dicom_series_instance_uid: NotRequired[
        "capo_medical_imaging.types.dicom_series_instance_uid.DICOMSeriesInstanceUID"
    ]
    """<p>The DICOM provided identifier for the Series Instance UID.</p>"""
    dicom_series_modality: NotRequired[
        "capo_medical_imaging.types.dicom_series_modality.DICOMSeriesModality"
    ]
    """<p>The DICOM provided identifier for the series Modality.</p>"""
    dicom_series_body_part: NotRequired[
        "capo_medical_imaging.types.dicom_series_body_part.DICOMSeriesBodyPart"
    ]
    """<p>The DICOM provided identifier for the series Body Part Examined.</p>"""
    dicom_series_number: NotRequired[
        "capo_medical_imaging.types.dicom_series_number.DICOMSeriesNumber"
    ]
    """<p>The DICOM provided identifier for the Series Number.</p>"""
    dicom_study_date: NotRequired[
        "capo_medical_imaging.types.dicom_study_date.DICOMStudyDate"
    ]
    """<p>The study date.</p>"""
    dicom_study_time: NotRequired[
        "capo_medical_imaging.types.dicom_study_time.DICOMStudyTime"
    ]
    """<p>The study time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DICOMTags) -> dict:
    out: dict = {}
    if "dicom_patient_id" in value:
        out["DICOMPatientId"] = value["dicom_patient_id"]
    if "dicom_patient_name" in value:
        out["DICOMPatientName"] = value["dicom_patient_name"]
    if "dicom_patient_birth_date" in value:
        out["DICOMPatientBirthDate"] = value["dicom_patient_birth_date"]
    if "dicom_patient_sex" in value:
        out["DICOMPatientSex"] = value["dicom_patient_sex"]
    if "dicom_study_instance_uid" in value:
        out["DICOMStudyInstanceUID"] = value["dicom_study_instance_uid"]
    if "dicom_study_id" in value:
        out["DICOMStudyId"] = value["dicom_study_id"]
    if "dicom_study_description" in value:
        out["DICOMStudyDescription"] = value["dicom_study_description"]
    out["DICOMNumberOfStudyRelatedSeries"] = value.get(
        "dicom_number_of_study_related_series", 0
    )
    out["DICOMNumberOfStudyRelatedInstances"] = value.get(
        "dicom_number_of_study_related_instances", 0
    )
    if "dicom_accession_number" in value:
        out["DICOMAccessionNumber"] = value["dicom_accession_number"]
    if "dicom_series_instance_uid" in value:
        out["DICOMSeriesInstanceUID"] = value["dicom_series_instance_uid"]
    if "dicom_series_modality" in value:
        out["DICOMSeriesModality"] = value["dicom_series_modality"]
    if "dicom_series_body_part" in value:
        out["DICOMSeriesBodyPart"] = value["dicom_series_body_part"]
    if "dicom_series_number" in value:
        out["DICOMSeriesNumber"] = value["dicom_series_number"]
    if "dicom_study_date" in value:
        out["DICOMStudyDate"] = value["dicom_study_date"]
    if "dicom_study_time" in value:
        out["DICOMStudyTime"] = value["dicom_study_time"]
    return out


def deserialize_json(data: dict) -> DICOMTags:
    out: DICOMTags = {}  # type: ignore[typeddict-item]
    if "DICOMPatientId" in data:
        out["dicom_patient_id"] = data["DICOMPatientId"]
    if "DICOMPatientName" in data:
        out["dicom_patient_name"] = data["DICOMPatientName"]
    if "DICOMPatientBirthDate" in data:
        out["dicom_patient_birth_date"] = data["DICOMPatientBirthDate"]
    if "DICOMPatientSex" in data:
        out["dicom_patient_sex"] = data["DICOMPatientSex"]
    if "DICOMStudyInstanceUID" in data:
        out["dicom_study_instance_uid"] = data["DICOMStudyInstanceUID"]
    if "DICOMStudyId" in data:
        out["dicom_study_id"] = data["DICOMStudyId"]
    if "DICOMStudyDescription" in data:
        out["dicom_study_description"] = data["DICOMStudyDescription"]
    if "DICOMNumberOfStudyRelatedSeries" in data:
        out["dicom_number_of_study_related_series"] = data[
            "DICOMNumberOfStudyRelatedSeries"
        ]
    else:
        out["dicom_number_of_study_related_series"] = 0
    if "DICOMNumberOfStudyRelatedInstances" in data:
        out["dicom_number_of_study_related_instances"] = data[
            "DICOMNumberOfStudyRelatedInstances"
        ]
    else:
        out["dicom_number_of_study_related_instances"] = 0
    if "DICOMAccessionNumber" in data:
        out["dicom_accession_number"] = data["DICOMAccessionNumber"]
    if "DICOMSeriesInstanceUID" in data:
        out["dicom_series_instance_uid"] = data["DICOMSeriesInstanceUID"]
    if "DICOMSeriesModality" in data:
        out["dicom_series_modality"] = data["DICOMSeriesModality"]
    if "DICOMSeriesBodyPart" in data:
        out["dicom_series_body_part"] = data["DICOMSeriesBodyPart"]
    if "DICOMSeriesNumber" in data:
        out["dicom_series_number"] = data["DICOMSeriesNumber"]
    if "DICOMStudyDate" in data:
        out["dicom_study_date"] = data["DICOMStudyDate"]
    if "DICOMStudyTime" in data:
        out["dicom_study_time"] = data["DICOMStudyTime"]
    return out
