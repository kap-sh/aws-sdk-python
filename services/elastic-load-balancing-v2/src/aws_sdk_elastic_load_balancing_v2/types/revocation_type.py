"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RevocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

RevocationType: TypeAlias = Literal["CRL",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("CRL",))


def to_query_text(value: RevocationType) -> str:
    return value


def from_query_text(text: str) -> RevocationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RevocationType value: {text!r}")
    return cast(RevocationType, text)


def serialize_query(
    value: RevocationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RevocationType:
    return from_query_text(el.text or "")
