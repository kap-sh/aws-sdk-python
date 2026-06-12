"""Generated from Smithy shape ``com.amazonaws.rds#ReservedDBInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.reserved_db_instance

ReservedDBInstanceList: TypeAlias = list[
    "aws_sdk_rds.types.reserved_db_instance.ReservedDBInstance"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedDBInstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.reserved_db_instance

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.reserved_db_instance.serialize_query(
            item, pairs, f"{prefix}.ReservedDBInstance.{n}"
        )


def deserialize_query(el: Element) -> ReservedDBInstanceList:
    import aws_sdk_rds.types.reserved_db_instance

    out: ReservedDBInstanceList = []
    for child in el.findall("ReservedDBInstance"):
        out.append(aws_sdk_rds.types.reserved_db_instance.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReservedDBInstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.reserved_db_instance

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.reserved_db_instance.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReservedDBInstanceList:
    import aws_sdk_rds.types.reserved_db_instance

    out: ReservedDBInstanceList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.reserved_db_instance.deserialize_query(child))
    return out
