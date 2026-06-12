"""Generated from Smithy shape ``com.amazonaws.neptune#DBInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_instance

DBInstanceList: TypeAlias = list["aws_sdk_neptune.types.db_instance.DBInstance"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.db_instance

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.db_instance.serialize_query(
            item, pairs, f"{prefix}.DBInstance.{n}"
        )


def deserialize_query(el: Element) -> DBInstanceList:
    import aws_sdk_neptune.types.db_instance

    out: DBInstanceList = []
    for child in el.findall("DBInstance"):
        out.append(aws_sdk_neptune.types.db_instance.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBInstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.db_instance

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.db_instance.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBInstanceList:
    import aws_sdk_neptune.types.db_instance

    out: DBInstanceList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_neptune.types.db_instance.deserialize_query(child))
    return out
