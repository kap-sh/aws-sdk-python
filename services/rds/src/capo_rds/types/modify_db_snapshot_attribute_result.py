"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBSnapshotAttributeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_snapshot_attributes_result


class ModifyDBSnapshotAttributeResult(TypedDict, closed=True):
    db_snapshot_attributes_result: NotRequired[
        "capo_rds.types.db_snapshot_attributes_result.DBSnapshotAttributesResult"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBSnapshotAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_snapshot_attributes_result" in value:
        import capo_rds.types.db_snapshot_attributes_result

        capo_rds.types.db_snapshot_attributes_result.serialize_query(
            value["db_snapshot_attributes_result"],
            pairs,
            f"{prefix}.DBSnapshotAttributesResult",
        )


def deserialize_query(el: Element) -> ModifyDBSnapshotAttributeResult:
    out: ModifyDBSnapshotAttributeResult = {}  # type: ignore[typeddict-item]
    child_db_snapshot_attributes_result = el.find("DBSnapshotAttributesResult")
    if child_db_snapshot_attributes_result is not None:
        import capo_rds.types.db_snapshot_attributes_result

        out["db_snapshot_attributes_result"] = (
            capo_rds.types.db_snapshot_attributes_result.deserialize_query(
                child_db_snapshot_attributes_result
            )
        )
    return out
