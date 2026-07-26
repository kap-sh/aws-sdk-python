"""Generated from Smithy shape ``com.amazonaws.neptune#ModifyDBInstanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_instance


class ModifyDBInstanceResult(TypedDict, closed=True):
    db_instance: NotRequired["capo_neptune.types.db_instance.DBInstance"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBInstanceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance" in value:
        import capo_neptune.types.db_instance

        capo_neptune.types.db_instance.serialize_query(
            value["db_instance"], pairs, f"{prefix}.DBInstance"
        )


def deserialize_query(el: Element) -> ModifyDBInstanceResult:
    out: ModifyDBInstanceResult = {}  # type: ignore[typeddict-item]
    child_db_instance = el.find("DBInstance")
    if child_db_instance is not None:
        import capo_neptune.types.db_instance

        out["db_instance"] = capo_neptune.types.db_instance.deserialize_query(
            child_db_instance
        )
    return out
