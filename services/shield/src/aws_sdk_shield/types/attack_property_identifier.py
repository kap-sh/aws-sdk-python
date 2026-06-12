"""Generated from Smithy shape ``com.amazonaws.shield#AttackPropertyIdentifier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

AttackPropertyIdentifier: TypeAlias = Literal[
    "DESTINATION_URL",
    "REFERRER",
    "SOURCE_ASN",
    "SOURCE_COUNTRY",
    "SOURCE_IP_ADDRESS",
    "SOURCE_USER_AGENT",
    "WORDPRESS_PINGBACK_REFLECTOR",
    "WORDPRESS_PINGBACK_SOURCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DESTINATION_URL",
        "REFERRER",
        "SOURCE_ASN",
        "SOURCE_COUNTRY",
        "SOURCE_IP_ADDRESS",
        "SOURCE_USER_AGENT",
        "WORDPRESS_PINGBACK_REFLECTOR",
        "WORDPRESS_PINGBACK_SOURCE",
    )
)


def serialize_aws_json_1_1(value: AttackPropertyIdentifier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttackPropertyIdentifier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttackPropertyIdentifier value: {data!r}")
    return cast(AttackPropertyIdentifier, data)
