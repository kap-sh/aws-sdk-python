"""Generated from Smithy shape ``com.amazonaws.acm#AcmCertificateMetadataFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_acm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.certificate_export
    import aws_sdk_acm.types.certificate_managed_by
    import aws_sdk_acm.types.certificate_status
    import aws_sdk_acm.types.certificate_type
    import aws_sdk_acm.types.nullable_boolean
    import aws_sdk_acm.types.renewal_status
    import aws_sdk_acm.types.validation_method


class _AcmCertificateMetadataFilter_Status(TypedDict):
    Status: "aws_sdk_acm.types.certificate_status.CertificateStatus"


class _AcmCertificateMetadataFilter_RenewalStatus(TypedDict):
    RenewalStatus: "aws_sdk_acm.types.renewal_status.RenewalStatus"


class _AcmCertificateMetadataFilter_Type(TypedDict):
    Type: "aws_sdk_acm.types.certificate_type.CertificateType"


class _AcmCertificateMetadataFilter_InUse(TypedDict):
    InUse: "aws_sdk_acm.types.nullable_boolean.NullableBoolean"


class _AcmCertificateMetadataFilter_Exported(TypedDict):
    Exported: "aws_sdk_acm.types.nullable_boolean.NullableBoolean"


class _AcmCertificateMetadataFilter_ExportOption(TypedDict):
    ExportOption: "aws_sdk_acm.types.certificate_export.CertificateExport"


class _AcmCertificateMetadataFilter_ManagedBy(TypedDict):
    ManagedBy: "aws_sdk_acm.types.certificate_managed_by.CertificateManagedBy"


class _AcmCertificateMetadataFilter_ValidationMethod(TypedDict):
    ValidationMethod: "aws_sdk_acm.types.validation_method.ValidationMethod"


AcmCertificateMetadataFilter: TypeAlias = (
    _AcmCertificateMetadataFilter_Status
    | _AcmCertificateMetadataFilter_RenewalStatus
    | _AcmCertificateMetadataFilter_Type
    | _AcmCertificateMetadataFilter_InUse
    | _AcmCertificateMetadataFilter_Exported
    | _AcmCertificateMetadataFilter_ExportOption
    | _AcmCertificateMetadataFilter_ManagedBy
    | _AcmCertificateMetadataFilter_ValidationMethod
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmCertificateMetadataFilter) -> dict:
    if "Status" in value:
        import aws_sdk_acm.types.certificate_status

        return {
            "Status": aws_sdk_acm.types.certificate_status.serialize_aws_json_1_1(
                value["Status"]
            )
        }
    elif "RenewalStatus" in value:
        import aws_sdk_acm.types.renewal_status

        return {
            "RenewalStatus": aws_sdk_acm.types.renewal_status.serialize_aws_json_1_1(
                value["RenewalStatus"]
            )
        }
    elif "Type" in value:
        import aws_sdk_acm.types.certificate_type

        return {
            "Type": aws_sdk_acm.types.certificate_type.serialize_aws_json_1_1(
                value["Type"]
            )
        }
    elif "InUse" in value:
        return {"InUse": value["InUse"]}
    elif "Exported" in value:
        return {"Exported": value["Exported"]}
    elif "ExportOption" in value:
        import aws_sdk_acm.types.certificate_export

        return {
            "ExportOption": aws_sdk_acm.types.certificate_export.serialize_aws_json_1_1(
                value["ExportOption"]
            )
        }
    elif "ManagedBy" in value:
        import aws_sdk_acm.types.certificate_managed_by

        return {
            "ManagedBy": aws_sdk_acm.types.certificate_managed_by.serialize_aws_json_1_1(
                value["ManagedBy"]
            )
        }
    elif "ValidationMethod" in value:
        import aws_sdk_acm.types.validation_method

        return {
            "ValidationMethod": aws_sdk_acm.types.validation_method.serialize_aws_json_1_1(
                value["ValidationMethod"]
            )
        }
    else:
        raise SerializationError("AcmCertificateMetadataFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AcmCertificateMetadataFilter:
    if "Status" in data:
        import aws_sdk_acm.types.certificate_status

        return {
            "Status": aws_sdk_acm.types.certificate_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        }
    elif "RenewalStatus" in data:
        import aws_sdk_acm.types.renewal_status

        return {
            "RenewalStatus": aws_sdk_acm.types.renewal_status.deserialize_aws_json_1_1(
                data["RenewalStatus"]
            )
        }
    elif "Type" in data:
        import aws_sdk_acm.types.certificate_type

        return {
            "Type": aws_sdk_acm.types.certificate_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        }
    elif "InUse" in data:
        return {"InUse": data["InUse"]}
    elif "Exported" in data:
        return {"Exported": data["Exported"]}
    elif "ExportOption" in data:
        import aws_sdk_acm.types.certificate_export

        return {
            "ExportOption": aws_sdk_acm.types.certificate_export.deserialize_aws_json_1_1(
                data["ExportOption"]
            )
        }
    elif "ManagedBy" in data:
        import aws_sdk_acm.types.certificate_managed_by

        return {
            "ManagedBy": aws_sdk_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        }
    elif "ValidationMethod" in data:
        import aws_sdk_acm.types.validation_method

        return {
            "ValidationMethod": aws_sdk_acm.types.validation_method.deserialize_aws_json_1_1(
                data["ValidationMethod"]
            )
        }
    else:
        raise DeserializationError(
            "AcmCertificateMetadataFilter: no recognized variant key"
        )
