"""Generated from Smithy shape ``com.amazonaws.cloudformation#ThirdPartyType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ThirdPartyType: TypeAlias = Literal[
    "RESOURCE",
    "MODULE",
    "HOOK",
]


# --- awsQuery ser/de ---
def to_query_text(value: ThirdPartyType) -> str:
    return value


def from_query_text(text: str) -> ThirdPartyType:
    return cast(ThirdPartyType, text)


def serialize_query(
    value: ThirdPartyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ThirdPartyType:
    return from_query_text(el.text or "")
