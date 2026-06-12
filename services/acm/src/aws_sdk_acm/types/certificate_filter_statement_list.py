"""Generated from Smithy shape ``com.amazonaws.acm#CertificateFilterStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.certificate_filter_statement

CertificateFilterStatementList: TypeAlias = list[
    "aws_sdk_acm.types.certificate_filter_statement.CertificateFilterStatement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateFilterStatementList) -> list:
    import aws_sdk_acm.types.certificate_filter_statement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_acm.types.certificate_filter_statement.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateFilterStatementList:
    import aws_sdk_acm.types.certificate_filter_statement

    out: CertificateFilterStatementList = []
    for item in data:
        out.append(
            aws_sdk_acm.types.certificate_filter_statement.deserialize_aws_json_1_1(
                item
            )
        )
    return out
