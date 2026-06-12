"""Generated from Smithy shape ``com.amazonaws.acm#SearchCertificatesSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

"""<p>The order to sort search results.</p>"""
SearchCertificatesSortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_aws_json_1_1(value: SearchCertificatesSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SearchCertificatesSortOrder:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SearchCertificatesSortOrder value: {data!r}"
        )
    return cast(SearchCertificatesSortOrder, data)
