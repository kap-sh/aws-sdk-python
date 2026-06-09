"""Generated from Smithy shape ``com.amazonaws.iam#clientIDListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.client_id_type

clientIDListType: TypeAlias = list["aws_sdk_iam.types.client_id_type.clientIDType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: clientIDListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> clientIDListType:
    out: clientIDListType = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: clientIDListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> clientIDListType:
    out: clientIDListType = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
