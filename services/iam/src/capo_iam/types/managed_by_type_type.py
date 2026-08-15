"""Generated from Smithy shape ``com.amazonaws.iam#managedByTypeType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

managedByTypeType: TypeAlias = Literal["Service",]


# --- awsQuery ser/de ---
def to_query_text(value: managedByTypeType) -> str:
    return value


def from_query_text(text: str) -> managedByTypeType:
    return cast(managedByTypeType, text)


def serialize_query(
    value: managedByTypeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> managedByTypeType:
    return from_query_text(el.text or "")
