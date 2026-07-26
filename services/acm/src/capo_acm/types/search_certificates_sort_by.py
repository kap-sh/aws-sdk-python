"""Generated from Smithy shape ``com.amazonaws.acm#SearchCertificatesSortBy``."""

from typing import Literal, TypeAlias, cast

"""<p>The field to sort search results by.</p>"""
SearchCertificatesSortBy: TypeAlias = Literal[
    "CREATED_AT",
    "NOT_AFTER",
    "STATUS",
    "RENEWAL_STATUS",
    "EXPORTED",
    "IN_USE",
    "NOT_BEFORE",
    "KEY_ALGORITHM",
    "TYPE",
    "CERTIFICATE_ARN",
    "COMMON_NAME",
    "REVOKED_AT",
    "RENEWAL_ELIGIBILITY",
    "ISSUED_AT",
    "MANAGED_BY",
    "EXPORT_OPTION",
    "VALIDATION_METHOD",
    "IMPORTED_AT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchCertificatesSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SearchCertificatesSortBy:
    return cast(SearchCertificatesSortBy, data)
