"""Generated from Smithy shape ``com.amazonaws.ec2#UserTrustProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

UserTrustProviderType: TypeAlias = Literal[
    "iam-identity-center",
    "oidc",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "iam-identity-center",
        "oidc",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "iam-identity-center",
        "oidc",
    )
)


def to_ec2_query_text(value: UserTrustProviderType) -> str:
    return value


def from_ec2_query_text(text: str) -> UserTrustProviderType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown UserTrustProviderType value: {text!r}")
    return cast(UserTrustProviderType, text)


def serialize_ec2_query(
    value: UserTrustProviderType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> UserTrustProviderType:
    return from_ec2_query_text(el.text or "")
