"""Generated from Smithy shape ``com.amazonaws.rds#ReservedDBInstancesOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.reserved_db_instances_offering

ReservedDBInstancesOfferingList: TypeAlias = list[
    "aws_sdk_rds.types.reserved_db_instances_offering.ReservedDBInstancesOffering"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedDBInstancesOfferingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.reserved_db_instances_offering

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.reserved_db_instances_offering.serialize_query(
            item, pairs, f"{prefix}.ReservedDBInstancesOffering.{n}"
        )


def deserialize_query(el: Element) -> ReservedDBInstancesOfferingList:
    import aws_sdk_rds.types.reserved_db_instances_offering

    out: ReservedDBInstancesOfferingList = []
    for child in el.findall("ReservedDBInstancesOffering"):
        out.append(
            aws_sdk_rds.types.reserved_db_instances_offering.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ReservedDBInstancesOfferingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.reserved_db_instances_offering

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.reserved_db_instances_offering.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ReservedDBInstancesOfferingList:
    import aws_sdk_rds.types.reserved_db_instances_offering

    out: ReservedDBInstancesOfferingList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_rds.types.reserved_db_instances_offering.deserialize_query(child)
        )
    return out
