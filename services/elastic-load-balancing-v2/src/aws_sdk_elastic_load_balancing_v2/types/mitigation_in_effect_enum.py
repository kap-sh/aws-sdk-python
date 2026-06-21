"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#MitigationInEffectEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

MitigationInEffectEnum: TypeAlias = Literal[
    "yes",
    "no",
]


# --- awsQuery ser/de ---
def to_query_text(value: MitigationInEffectEnum) -> str:
    return value


def from_query_text(text: str) -> MitigationInEffectEnum:
    return cast(MitigationInEffectEnum, text)


def serialize_query(
    value: MitigationInEffectEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MitigationInEffectEnum:
    return from_query_text(el.text or "")
