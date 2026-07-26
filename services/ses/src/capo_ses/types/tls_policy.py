"""Generated from Smithy shape ``com.amazonaws.ses#TlsPolicy``."""

from typing import Literal, TypeAlias, cast

from capo_ses._protocol.xml import Element

TlsPolicy: TypeAlias = Literal[
    "Require",
    "Optional",
]


# --- awsQuery ser/de ---
def to_query_text(value: TlsPolicy) -> str:
    return value


def from_query_text(text: str) -> TlsPolicy:
    return cast(TlsPolicy, text)


def serialize_query(
    value: TlsPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TlsPolicy:
    return from_query_text(el.text or "")
