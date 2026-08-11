"""Generated from Smithy shape ``com.amazonaws.iam#policyNameListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_name_type

policyNameListType: TypeAlias = list["capo_iam.types.policy_name_type.policyNameType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: policyNameListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> policyNameListType:
    out: policyNameListType = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: policyNameListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> policyNameListType:
    out: policyNameListType = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
