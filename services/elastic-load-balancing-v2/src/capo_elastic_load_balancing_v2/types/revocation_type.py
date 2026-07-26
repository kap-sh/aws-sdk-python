"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RevocationType``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

RevocationType: TypeAlias = Literal["CRL",]


# --- awsQuery ser/de ---
def to_query_text(value: RevocationType) -> str:
    return value


def from_query_text(text: str) -> RevocationType:
    return cast(RevocationType, text)


def serialize_query(
    value: RevocationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RevocationType:
    return from_query_text(el.text or "")
