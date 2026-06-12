"""Generated from Smithy shape ``com.amazonaws.rds#PurchaseReservedDBInstancesOfferingResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.reserved_db_instance


class PurchaseReservedDBInstancesOfferingResult(TypedDict):
    reserved_db_instance: NotRequired[
        "aws_sdk_rds.types.reserved_db_instance.ReservedDBInstance"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: PurchaseReservedDBInstancesOfferingResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_db_instance" in value:
        import aws_sdk_rds.types.reserved_db_instance

        aws_sdk_rds.types.reserved_db_instance.serialize_query(
            value["reserved_db_instance"], pairs, f"{prefix}.ReservedDBInstance"
        )


def deserialize_query(el: Element) -> PurchaseReservedDBInstancesOfferingResult:
    out: PurchaseReservedDBInstancesOfferingResult = {}  # type: ignore[typeddict-item]
    child_reserved_db_instance = el.find("ReservedDBInstance")
    if child_reserved_db_instance is not None:
        import aws_sdk_rds.types.reserved_db_instance

        out["reserved_db_instance"] = (
            aws_sdk_rds.types.reserved_db_instance.deserialize_query(
                child_reserved_db_instance
            )
        )
    return out
