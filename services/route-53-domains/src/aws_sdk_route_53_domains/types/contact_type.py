"""Generated from Smithy shape ``com.amazonaws.route53domains#ContactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

ContactType: TypeAlias = Literal[
    "PERSON",
    "COMPANY",
    "ASSOCIATION",
    "PUBLIC_BODY",
    "RESELLER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERSON",
        "COMPANY",
        "ASSOCIATION",
        "PUBLIC_BODY",
        "RESELLER",
    )
)


def serialize_aws_json_1_1(value: ContactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactType value: {data!r}")
    return cast(ContactType, data)
