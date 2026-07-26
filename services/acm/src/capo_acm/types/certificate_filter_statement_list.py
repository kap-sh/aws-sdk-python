"""Generated from Smithy shape ``com.amazonaws.acm#CertificateFilterStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.certificate_filter_statement

CertificateFilterStatementList: TypeAlias = list[
    "capo_acm.types.certificate_filter_statement.CertificateFilterStatement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateFilterStatementList) -> list:
    import capo_acm.types.certificate_filter_statement

    out: list = []
    for item in value:
        out.append(
            capo_acm.types.certificate_filter_statement.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateFilterStatementList:
    import capo_acm.types.certificate_filter_statement

    out: CertificateFilterStatementList = []
    for item in data:
        out.append(
            capo_acm.types.certificate_filter_statement.deserialize_aws_json_1_1(item)
        )
    return out
