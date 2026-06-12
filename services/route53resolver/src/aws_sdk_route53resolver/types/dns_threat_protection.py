"""Generated from Smithy shape ``com.amazonaws.route53resolver#DnsThreatProtection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

DnsThreatProtection: TypeAlias = Literal[
    "DGA",
    "DNS_TUNNELING",
    "DICTIONARY_DGA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DGA",
        "DNS_TUNNELING",
        "DICTIONARY_DGA",
    )
)


def serialize_aws_json_1_1(value: DnsThreatProtection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DnsThreatProtection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DnsThreatProtection value: {data!r}")
    return cast(DnsThreatProtection, data)
