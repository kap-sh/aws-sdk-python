"""Generated from Smithy shape ``com.amazonaws.cloudformation#EvaluationType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

EvaluationType: TypeAlias = Literal[
    "Static",
    "Dynamic",
]


# --- awsQuery ser/de ---
def to_query_text(value: EvaluationType) -> str:
    return value


def from_query_text(text: str) -> EvaluationType:
    return cast(EvaluationType, text)


def serialize_query(
    value: EvaluationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EvaluationType:
    return from_query_text(el.text or "")
