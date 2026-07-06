"""Generated from Smithy shape ``com.amazonaws.acm#ListCertificatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.certificate_summary_list
    import aws_sdk_acm.types.next_token


class ListCertificatesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_acm.types.next_token.NextToken"]
    """<p>When the list is truncated, this value is present and contains the value to use for the <code>NextToken</code> parameter in a subsequent pagination request.</p>"""
    certificate_summary_list: NotRequired[
        "aws_sdk_acm.types.certificate_summary_list.CertificateSummaryList"
    ]
    """<p>A list of ACM certificates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "certificate_summary_list" in value:
        import aws_sdk_acm.types.certificate_summary_list

        out["CertificateSummaryList"] = (
            aws_sdk_acm.types.certificate_summary_list.serialize_aws_json_1_1(
                value["certificate_summary_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificatesResponse:
    out: ListCertificatesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "CertificateSummaryList" in data:
        import aws_sdk_acm.types.certificate_summary_list

        out["certificate_summary_list"] = (
            aws_sdk_acm.types.certificate_summary_list.deserialize_aws_json_1_1(
                data["CertificateSummaryList"]
            )
        )
    return out
