"""Generated from Smithy shape ``com.amazonaws.acm#SearchCertificatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.certificate_search_result_list
    import capo_acm.types.next_token


class SearchCertificatesResponse(TypedDict, closed=True):
    results: NotRequired[
        "capo_acm.types.certificate_search_result_list.CertificateSearchResultList"
    ]
    """<p>A list of certificate search results containing certificate ARNs, X.509 attributes, and ACM metadata.</p>"""
    next_token: NotRequired["capo_acm.types.next_token.NextToken"]
    """<p>When the list is truncated, this value is present and contains the value to use for the <code>NextToken</code> parameter in a subsequent pagination request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchCertificatesResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_acm.types.certificate_search_result_list

        out["Results"] = (
            capo_acm.types.certificate_search_result_list.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchCertificatesResponse:
    out: SearchCertificatesResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_acm.types.certificate_search_result_list

        out["results"] = (
            capo_acm.types.certificate_search_result_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
