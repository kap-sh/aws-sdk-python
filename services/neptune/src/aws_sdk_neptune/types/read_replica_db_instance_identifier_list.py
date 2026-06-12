"""Generated from Smithy shape ``com.amazonaws.neptune#ReadReplicaDBInstanceIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string

ReadReplicaDBInstanceIdentifierList: TypeAlias = list[
    "aws_sdk_neptune.types.string.String"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReadReplicaDBInstanceIdentifierList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.ReadReplicaDBInstanceIdentifier.{n}", str(item)))


def deserialize_query(el: Element) -> ReadReplicaDBInstanceIdentifierList:
    out: ReadReplicaDBInstanceIdentifierList = []
    for child in el.findall("ReadReplicaDBInstanceIdentifier"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ReadReplicaDBInstanceIdentifierList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(
    parent: Element, tag: str
) -> ReadReplicaDBInstanceIdentifierList:
    out: ReadReplicaDBInstanceIdentifierList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
