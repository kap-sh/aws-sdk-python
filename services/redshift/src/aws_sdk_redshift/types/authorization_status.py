"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

AuthorizationStatus: TypeAlias = Literal[
    "Authorized",
    "Revoking",
]


# --- awsQuery ser/de ---
def to_query_text(value: AuthorizationStatus) -> str:
    return value


def from_query_text(text: str) -> AuthorizationStatus:
    return cast(AuthorizationStatus, text)


def serialize_query(
    value: AuthorizationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuthorizationStatus:
    return from_query_text(el.text or "")
