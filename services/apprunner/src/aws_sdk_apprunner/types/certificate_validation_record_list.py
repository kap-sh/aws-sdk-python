"""Generated from Smithy shape ``com.amazonaws.apprunner#CertificateValidationRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.certificate_validation_record

CertificateValidationRecordList: TypeAlias = list[
    "aws_sdk_apprunner.types.certificate_validation_record.CertificateValidationRecord"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CertificateValidationRecordList) -> list:
    import aws_sdk_apprunner.types.certificate_validation_record

    out: list = []
    for item in value:
        out.append(
            aws_sdk_apprunner.types.certificate_validation_record.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CertificateValidationRecordList:
    import aws_sdk_apprunner.types.certificate_validation_record

    out: CertificateValidationRecordList = []
    for item in data:
        out.append(
            aws_sdk_apprunner.types.certificate_validation_record.deserialize_aws_json_1_0(
                item
            )
        )
    return out
