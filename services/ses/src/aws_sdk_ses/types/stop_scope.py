"""Generated from Smithy shape ``com.amazonaws.ses#StopScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

StopScope: TypeAlias = Literal["RuleSet",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("RuleSet",))


def to_query_text(value: StopScope) -> str:
    return value


def from_query_text(text: str) -> StopScope:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StopScope value: {text!r}")
    return cast(StopScope, text)


def serialize_query(
    value: StopScope, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StopScope:
    return from_query_text(el.text or "")
