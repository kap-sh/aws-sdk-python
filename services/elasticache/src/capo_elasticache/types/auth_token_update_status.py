"""Generated from Smithy shape ``com.amazonaws.elasticache#AuthTokenUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

AuthTokenUpdateStatus: TypeAlias = Literal[
    "SETTING",
    "ROTATING",
]


# --- awsQuery ser/de ---
def to_query_text(value: AuthTokenUpdateStatus) -> str:
    return value


def from_query_text(text: str) -> AuthTokenUpdateStatus:
    return cast(AuthTokenUpdateStatus, text)


def serialize_query(
    value: AuthTokenUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthTokenUpdateStatus:
    return from_query_text(el.text or "")
