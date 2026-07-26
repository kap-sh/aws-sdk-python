"""Generated from Smithy shape ``com.amazonaws.iam#ContextKeyValueListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.context_key_value_type

ContextKeyValueListType: TypeAlias = list[
    "capo_iam.types.context_key_value_type.ContextKeyValueType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ContextKeyValueListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> ContextKeyValueListType:
    out: ContextKeyValueListType = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ContextKeyValueListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ContextKeyValueListType:
    out: ContextKeyValueListType = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
