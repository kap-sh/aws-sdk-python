"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AnomalyResultEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

AnomalyResultEnum: TypeAlias = Literal[
    "anomalous",
    "normal",
]


# --- awsQuery ser/de ---
def to_query_text(value: AnomalyResultEnum) -> str:
    return value


def from_query_text(text: str) -> AnomalyResultEnum:
    return cast(AnomalyResultEnum, text)


def serialize_query(
    value: AnomalyResultEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnomalyResultEnum:
    return from_query_text(el.text or "")
