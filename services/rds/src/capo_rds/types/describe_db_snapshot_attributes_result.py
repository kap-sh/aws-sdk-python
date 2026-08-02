"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBSnapshotAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_snapshot_attributes_result


class DescribeDBSnapshotAttributesResult(TypedDict, closed=True):
    db_snapshot_attributes_result: NotRequired[
        "capo_rds.types.db_snapshot_attributes_result.DBSnapshotAttributesResult"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBSnapshotAttributesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_snapshot_attributes_result" in value:
        import capo_rds.types.db_snapshot_attributes_result

        capo_rds.types.db_snapshot_attributes_result.serialize_query(
            value["db_snapshot_attributes_result"],
            pairs,
            f"{key_prefix}DBSnapshotAttributesResult",
        )


def deserialize_query(el: Element) -> DescribeDBSnapshotAttributesResult:
    out: DescribeDBSnapshotAttributesResult = {}  # type: ignore[typeddict-item]
    child_db_snapshot_attributes_result = el.find("DBSnapshotAttributesResult")
    if child_db_snapshot_attributes_result is not None:
        import capo_rds.types.db_snapshot_attributes_result

        out["db_snapshot_attributes_result"] = (
            capo_rds.types.db_snapshot_attributes_result.deserialize_query(
                child_db_snapshot_attributes_result
            )
        )
    return out
