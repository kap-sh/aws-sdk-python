"""Generated from Smithy shape ``com.amazonaws.neptune#OrderableDBInstanceOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.orderable_db_instance_option

OrderableDBInstanceOptionsList: TypeAlias = list[
    "aws_sdk_neptune.types.orderable_db_instance_option.OrderableDBInstanceOption"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableDBInstanceOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.orderable_db_instance_option

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.orderable_db_instance_option.serialize_query(
            item, pairs, f"{prefix}.OrderableDBInstanceOption.{n}"
        )


def deserialize_query(el: Element) -> OrderableDBInstanceOptionsList:
    import aws_sdk_neptune.types.orderable_db_instance_option

    out: OrderableDBInstanceOptionsList = []
    for child in el.findall("OrderableDBInstanceOption"):
        out.append(
            aws_sdk_neptune.types.orderable_db_instance_option.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: OrderableDBInstanceOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.orderable_db_instance_option

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.orderable_db_instance_option.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OrderableDBInstanceOptionsList:
    import aws_sdk_neptune.types.orderable_db_instance_option

    out: OrderableDBInstanceOptionsList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_neptune.types.orderable_db_instance_option.deserialize_query(child)
        )
    return out
