"""Generated from Smithy shape ``com.amazonaws.docdb#ModifyDBInstanceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_instance


class ModifyDBInstanceResult(TypedDict):
    db_instance: NotRequired["aws_sdk_docdb.types.db_instance.DBInstance"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBInstanceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance" in value:
        import aws_sdk_docdb.types.db_instance

        aws_sdk_docdb.types.db_instance.serialize_query(
            value["db_instance"], pairs, f"{prefix}.DBInstance"
        )


def deserialize_query(el: Element) -> ModifyDBInstanceResult:
    out: ModifyDBInstanceResult = {}  # type: ignore[typeddict-item]
    child_db_instance = el.find("DBInstance")
    if child_db_instance is not None:
        import aws_sdk_docdb.types.db_instance

        out["db_instance"] = aws_sdk_docdb.types.db_instance.deserialize_query(
            child_db_instance
        )
    return out
