"""Generated from Smithy shape ``com.amazonaws.ses#AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.address

AddressList: TypeAlias = list["capo_ses.types.address.Address"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> AddressList:
    out: AddressList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: AddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> AddressList:
    out: AddressList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
