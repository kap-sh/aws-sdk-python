"""Generated from Smithy shape ``com.amazonaws.rds#AuthScheme``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

AuthScheme: TypeAlias = Literal["SECRETS",]


# --- awsQuery ser/de ---
def to_query_text(value: AuthScheme) -> str:
    return value


def from_query_text(text: str) -> AuthScheme:
    return cast(AuthScheme, text)


def serialize_query(
    value: AuthScheme, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthScheme:
    return from_query_text(el.text or "")
