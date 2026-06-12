"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AuthenticateCognitoActionConditionalBehaviorEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

AuthenticateCognitoActionConditionalBehaviorEnum: TypeAlias = Literal[
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


def to_query_text(value: AuthenticateCognitoActionConditionalBehaviorEnum) -> str:
    return value


def from_query_text(text: str) -> AuthenticateCognitoActionConditionalBehaviorEnum:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown AuthenticateCognitoActionConditionalBehaviorEnum value: {text!r}"
        )
    return cast(AuthenticateCognitoActionConditionalBehaviorEnum, text)


def serialize_query(
    value: AuthenticateCognitoActionConditionalBehaviorEnum,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthenticateCognitoActionConditionalBehaviorEnum:
    return from_query_text(el.text or "")
