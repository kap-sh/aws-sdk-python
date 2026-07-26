"""Generated from Smithy shape ``com.amazonaws.autoscaling#RetryStrategy``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

RetryStrategy: TypeAlias = Literal[
    "retry-with-group-configuration",
    "none",
]


# --- awsQuery ser/de ---
def to_query_text(value: RetryStrategy) -> str:
    return value


def from_query_text(text: str) -> RetryStrategy:
    return cast(RetryStrategy, text)


def serialize_query(
    value: RetryStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RetryStrategy:
    return from_query_text(el.text or "")
