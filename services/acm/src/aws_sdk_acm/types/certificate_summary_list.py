"""Generated from Smithy shape ``com.amazonaws.acm#CertificateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.certificate_summary

CertificateSummaryList: TypeAlias = list[
    "aws_sdk_acm.types.certificate_summary.CertificateSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateSummaryList) -> list:
    import aws_sdk_acm.types.certificate_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_acm.types.certificate_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateSummaryList:
    import aws_sdk_acm.types.certificate_summary

    out: CertificateSummaryList = []
    for item in data:
        out.append(aws_sdk_acm.types.certificate_summary.deserialize_aws_json_1_1(item))
    return out
