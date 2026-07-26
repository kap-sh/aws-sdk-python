"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ActionTypeEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

ActionTypeEnum: TypeAlias = Literal[
    "forward",
    "authenticate-oidc",
    "authenticate-cognito",
    "redirect",
    "fixed-response",
    "jwt-validation",
]


# --- awsQuery ser/de ---
def to_query_text(value: ActionTypeEnum) -> str:
    return value


def from_query_text(text: str) -> ActionTypeEnum:
    return cast(ActionTypeEnum, text)


def serialize_query(
    value: ActionTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ActionTypeEnum:
    return from_query_text(el.text or "")
