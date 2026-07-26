"""Generated from Smithy shape ``com.amazonaws.ses#StopScope``."""

from typing import Literal, TypeAlias, cast

from capo_ses._protocol.xml import Element

StopScope: TypeAlias = Literal["RuleSet",]


# --- awsQuery ser/de ---
def to_query_text(value: StopScope) -> str:
    return value


def from_query_text(text: str) -> StopScope:
    return cast(StopScope, text)


def serialize_query(
    value: StopScope, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StopScope:
    return from_query_text(el.text or "")
