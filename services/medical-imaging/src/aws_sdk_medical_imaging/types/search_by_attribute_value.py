"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchByAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.dicom_accession_number
    import aws_sdk_medical_imaging.types.dicom_patient_id
    import aws_sdk_medical_imaging.types.dicom_series_instance_uid
    import aws_sdk_medical_imaging.types.dicom_study_date_and_time
    import aws_sdk_medical_imaging.types.dicom_study_id
    import aws_sdk_medical_imaging.types.dicom_study_instance_uid


class _SearchByAttributeValue_DICOMPatientId(TypedDict):
    DICOMPatientId: "aws_sdk_medical_imaging.types.dicom_patient_id.DICOMPatientId"


class _SearchByAttributeValue_DICOMAccessionNumber(TypedDict):
    DICOMAccessionNumber: (
        "aws_sdk_medical_imaging.types.dicom_accession_number.DICOMAccessionNumber"
    )


class _SearchByAttributeValue_DICOMStudyId(TypedDict):
    DICOMStudyId: "aws_sdk_medical_imaging.types.dicom_study_id.DICOMStudyId"


class _SearchByAttributeValue_DICOMStudyInstanceUID(TypedDict):
    DICOMStudyInstanceUID: (
        "aws_sdk_medical_imaging.types.dicom_study_instance_uid.DICOMStudyInstanceUID"
    )


class _SearchByAttributeValue_DICOMSeriesInstanceUID(TypedDict):
    DICOMSeriesInstanceUID: (
        "aws_sdk_medical_imaging.types.dicom_series_instance_uid.DICOMSeriesInstanceUID"
    )


class _SearchByAttributeValue_createdAt(TypedDict):
    createdAt: "aws_sdk_medical_imaging.types.date.Date"


class _SearchByAttributeValue_updatedAt(TypedDict):
    updatedAt: "aws_sdk_medical_imaging.types.date.Date"


class _SearchByAttributeValue_DICOMStudyDateAndTime(TypedDict):
    DICOMStudyDateAndTime: (
        "aws_sdk_medical_imaging.types.dicom_study_date_and_time.DICOMStudyDateAndTime"
    )


class _SearchByAttributeValue_isPrimary(TypedDict):
    isPrimary: "bool"


SearchByAttributeValue: TypeAlias = (
    _SearchByAttributeValue_DICOMPatientId
    | _SearchByAttributeValue_DICOMAccessionNumber
    | _SearchByAttributeValue_DICOMStudyId
    | _SearchByAttributeValue_DICOMStudyInstanceUID
    | _SearchByAttributeValue_DICOMSeriesInstanceUID
    | _SearchByAttributeValue_createdAt
    | _SearchByAttributeValue_updatedAt
    | _SearchByAttributeValue_DICOMStudyDateAndTime
    | _SearchByAttributeValue_isPrimary
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchByAttributeValue) -> dict:
    if "DICOMPatientId" in value:
        return {"DICOMPatientId": value["DICOMPatientId"]}
    elif "DICOMAccessionNumber" in value:
        return {"DICOMAccessionNumber": value["DICOMAccessionNumber"]}
    elif "DICOMStudyId" in value:
        return {"DICOMStudyId": value["DICOMStudyId"]}
    elif "DICOMStudyInstanceUID" in value:
        return {"DICOMStudyInstanceUID": value["DICOMStudyInstanceUID"]}
    elif "DICOMSeriesInstanceUID" in value:
        return {"DICOMSeriesInstanceUID": value["DICOMSeriesInstanceUID"]}
    elif "createdAt" in value:
        import aws_sdk_medical_imaging.types.date

        return {
            "createdAt": aws_sdk_medical_imaging.types.date.serialize_json(
                value["createdAt"]
            )
        }
    elif "updatedAt" in value:
        import aws_sdk_medical_imaging.types.date

        return {
            "updatedAt": aws_sdk_medical_imaging.types.date.serialize_json(
                value["updatedAt"]
            )
        }
    elif "DICOMStudyDateAndTime" in value:
        import aws_sdk_medical_imaging.types.dicom_study_date_and_time

        return {
            "DICOMStudyDateAndTime": aws_sdk_medical_imaging.types.dicom_study_date_and_time.serialize_json(
                value["DICOMStudyDateAndTime"]
            )
        }
    elif "isPrimary" in value:
        return {"isPrimary": value["isPrimary"]}
    else:
        raise SerializationError("SearchByAttributeValue: no variant present")


def deserialize_json(data: dict) -> SearchByAttributeValue:
    if "DICOMPatientId" in data:
        return {"DICOMPatientId": data["DICOMPatientId"]}
    elif "DICOMAccessionNumber" in data:
        return {"DICOMAccessionNumber": data["DICOMAccessionNumber"]}
    elif "DICOMStudyId" in data:
        return {"DICOMStudyId": data["DICOMStudyId"]}
    elif "DICOMStudyInstanceUID" in data:
        return {"DICOMStudyInstanceUID": data["DICOMStudyInstanceUID"]}
    elif "DICOMSeriesInstanceUID" in data:
        return {"DICOMSeriesInstanceUID": data["DICOMSeriesInstanceUID"]}
    elif "createdAt" in data:
        import aws_sdk_medical_imaging.types.date

        return {
            "createdAt": aws_sdk_medical_imaging.types.date.deserialize_json(
                data["createdAt"]
            )
        }
    elif "updatedAt" in data:
        import aws_sdk_medical_imaging.types.date

        return {
            "updatedAt": aws_sdk_medical_imaging.types.date.deserialize_json(
                data["updatedAt"]
            )
        }
    elif "DICOMStudyDateAndTime" in data:
        import aws_sdk_medical_imaging.types.dicom_study_date_and_time

        return {
            "DICOMStudyDateAndTime": aws_sdk_medical_imaging.types.dicom_study_date_and_time.deserialize_json(
                data["DICOMStudyDateAndTime"]
            )
        }
    elif "isPrimary" in data:
        return {"isPrimary": data["isPrimary"]}
    else:
        raise DeserializationError("SearchByAttributeValue: no recognized variant key")
