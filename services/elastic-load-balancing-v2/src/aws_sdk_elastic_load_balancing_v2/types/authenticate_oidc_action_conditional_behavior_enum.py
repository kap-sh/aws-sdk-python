"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AuthenticateOidcActionConditionalBehaviorEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

AuthenticateOidcActionConditionalBehaviorEnum: TypeAlias = Literal[
    "deny",
    "allow",
    "authenticate",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "deny",
        "allow",
        "authenticate",
    )
)


def to_query_text(value: AuthenticateOidcActionConditionalBehaviorEnum) -> str:
    return value


def from_query_text(text: str) -> AuthenticateOidcActionConditionalBehaviorEnum:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown AuthenticateOidcActionConditionalBehaviorEnum value: {text!r}"
        )
    return cast(AuthenticateOidcActionConditionalBehaviorEnum, text)


def serialize_query(
    value: AuthenticateOidcActionConditionalBehaviorEnum,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthenticateOidcActionConditionalBehaviorEnum:
    return from_query_text(el.text or "")
