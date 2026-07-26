"""Generated from Smithy shape ``com.amazonaws.acm#SearchCertificatesSortOrder``."""

from typing import Literal, TypeAlias, cast

"""<p>The order to sort search results.</p>"""
SearchCertificatesSortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchCertificatesSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SearchCertificatesSortOrder:
    return cast(SearchCertificatesSortOrder, data)
