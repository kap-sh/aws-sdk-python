"""Generated from Smithy shape ``com.amazonaws.elasticache#SubnetIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string

SubnetIdsList: TypeAlias = list["aws_sdk_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.SubnetId.{n}", str(item)))


def deserialize_query(el: Element) -> SubnetIdsList:
    out: SubnetIdsList = []
    for child in el.findall("SubnetId"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: SubnetIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SubnetIdsList:
    out: SubnetIdsList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
