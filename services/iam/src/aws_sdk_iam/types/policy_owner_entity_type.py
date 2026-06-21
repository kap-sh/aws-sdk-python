"""Generated from Smithy shape ``com.amazonaws.iam#policyOwnerEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

policyOwnerEntityType: TypeAlias = Literal[
    "USER",
    "ROLE",
    "GROUP",
]


# --- awsQuery ser/de ---
def to_query_text(value: policyOwnerEntityType) -> str:
    return value


def from_query_text(text: str) -> policyOwnerEntityType:
    return cast(policyOwnerEntityType, text)


def serialize_query(
    value: policyOwnerEntityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> policyOwnerEntityType:
    return from_query_text(el.text or "")
