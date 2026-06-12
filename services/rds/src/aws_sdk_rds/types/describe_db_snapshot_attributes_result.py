"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBSnapshotAttributesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_snapshot_attributes_result


class DescribeDBSnapshotAttributesResult(TypedDict):
    db_snapshot_attributes_result: NotRequired[
        "aws_sdk_rds.types.db_snapshot_attributes_result.DBSnapshotAttributesResult"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBSnapshotAttributesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_snapshot_attributes_result" in value:
        import aws_sdk_rds.types.db_snapshot_attributes_result

        aws_sdk_rds.types.db_snapshot_attributes_result.serialize_query(
            value["db_snapshot_attributes_result"],
            pairs,
            f"{prefix}.DBSnapshotAttributesResult",
        )


def deserialize_query(el: Element) -> DescribeDBSnapshotAttributesResult:
    out: DescribeDBSnapshotAttributesResult = {}  # type: ignore[typeddict-item]
    child_db_snapshot_attributes_result = el.find("DBSnapshotAttributesResult")
    if child_db_snapshot_attributes_result is not None:
        import aws_sdk_rds.types.db_snapshot_attributes_result

        out["db_snapshot_attributes_result"] = (
            aws_sdk_rds.types.db_snapshot_attributes_result.deserialize_query(
                child_db_snapshot_attributes_result
            )
        )
    return out
