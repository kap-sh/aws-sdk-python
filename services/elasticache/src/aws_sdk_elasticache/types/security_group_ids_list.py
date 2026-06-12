"""Generated from Smithy shape ``com.amazonaws.elasticache#SecurityGroupIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string

SecurityGroupIdsList: TypeAlias = list["aws_sdk_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SecurityGroupIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.SecurityGroupId.{n}", str(item)))


def deserialize_query(el: Element) -> SecurityGroupIdsList:
    out: SecurityGroupIdsList = []
    for child in el.findall("SecurityGroupId"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: SecurityGroupIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SecurityGroupIdsList:
    out: SecurityGroupIdsList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
