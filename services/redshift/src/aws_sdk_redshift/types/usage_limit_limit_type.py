"""Generated from Smithy shape ``com.amazonaws.redshift#UsageLimitLimitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

UsageLimitLimitType: TypeAlias = Literal[
    "time",
    "data-scanned",
]


# --- awsQuery ser/de ---
def to_query_text(value: UsageLimitLimitType) -> str:
    return value


def from_query_text(text: str) -> UsageLimitLimitType:
    return cast(UsageLimitLimitType, text)


def serialize_query(
    value: UsageLimitLimitType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> UsageLimitLimitType:
    return from_query_text(el.text or "")
