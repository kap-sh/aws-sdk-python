"""Generated from Smithy shape ``com.amazonaws.elasticache#InputAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

InputAuthenticationType: TypeAlias = Literal[
    "password",
    "no-password-required",
    "iam",
]


# --- awsQuery ser/de ---
def to_query_text(value: InputAuthenticationType) -> str:
    return value


def from_query_text(text: str) -> InputAuthenticationType:
    return cast(InputAuthenticationType, text)


def serialize_query(
    value: InputAuthenticationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InputAuthenticationType:
    return from_query_text(el.text or "")
