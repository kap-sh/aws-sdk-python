"""Generated from Smithy shape ``com.amazonaws.elasticache#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

AuthenticationType: TypeAlias = Literal[
    "password",
    "no-password",
    "iam",
]


# --- awsQuery ser/de ---
def to_query_text(value: AuthenticationType) -> str:
    return value


def from_query_text(text: str) -> AuthenticationType:
    return cast(AuthenticationType, text)


def serialize_query(
    value: AuthenticationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthenticationType:
    return from_query_text(el.text or "")
