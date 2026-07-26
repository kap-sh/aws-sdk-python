"""Generated from Smithy shape ``com.amazonaws.sns#RouteType``."""

from typing import Literal, TypeAlias, cast

from capo_sns._protocol.xml import Element

"""Enum listing out all supported route types. The following enum values are supported. 1. Transactional : Non-marketing traffic 2. Promotional : Marketing 3. Premium : Premium routes for OTP delivery to the carriers"""
RouteType: TypeAlias = Literal[
    "Transactional",
    "Promotional",
    "Premium",
]


# --- awsQuery ser/de ---
def to_query_text(value: RouteType) -> str:
    return value


def from_query_text(text: str) -> RouteType:
    return cast(RouteType, text)


def serialize_query(
    value: RouteType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RouteType:
    return from_query_text(el.text or "")
