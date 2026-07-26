"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TransformTypeEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

TransformTypeEnum: TypeAlias = Literal[
    "host-header-rewrite",
    "url-rewrite",
]


# --- awsQuery ser/de ---
def to_query_text(value: TransformTypeEnum) -> str:
    return value


def from_query_text(text: str) -> TransformTypeEnum:
    return cast(TransformTypeEnum, text)


def serialize_query(
    value: TransformTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TransformTypeEnum:
    return from_query_text(el.text or "")
