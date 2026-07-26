"""Generated from Smithy shape ``com.amazonaws.redshift#UsageLimitPeriod``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

UsageLimitPeriod: TypeAlias = Literal[
    "daily",
    "weekly",
    "monthly",
]


# --- awsQuery ser/de ---
def to_query_text(value: UsageLimitPeriod) -> str:
    return value


def from_query_text(text: str) -> UsageLimitPeriod:
    return cast(UsageLimitPeriod, text)


def serialize_query(
    value: UsageLimitPeriod, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> UsageLimitPeriod:
    return from_query_text(el.text or "")
