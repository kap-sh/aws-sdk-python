"""Generated from Smithy shape ``com.amazonaws.acm#CertificateSearchResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.certificate_search_result

CertificateSearchResultList: TypeAlias = list[
    "capo_acm.types.certificate_search_result.CertificateSearchResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateSearchResultList) -> list:
    import capo_acm.types.certificate_search_result

    out: list = []
    for item in value:
        out.append(
            capo_acm.types.certificate_search_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateSearchResultList:
    import capo_acm.types.certificate_search_result

    out: CertificateSearchResultList = []
    for item in data:
        out.append(
            capo_acm.types.certificate_search_result.deserialize_aws_json_1_1(item)
        )
    return out
