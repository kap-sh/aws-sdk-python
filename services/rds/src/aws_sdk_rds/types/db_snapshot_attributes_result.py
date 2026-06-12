"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotAttributesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_snapshot_attribute_list
    import aws_sdk_rds.types.string


class DBSnapshotAttributesResult(TypedDict):
    db_snapshot_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The identifier of the manual DB snapshot that the attributes apply to.</p>"""
    db_snapshot_attributes: NotRequired[
        "aws_sdk_rds.types.db_snapshot_attribute_list.DBSnapshotAttributeList"
    ]
    """<p>The list of attributes and values for the manual DB snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotAttributesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "db_snapshot_attributes" in value:
        import aws_sdk_rds.types.db_snapshot_attribute_list

        aws_sdk_rds.types.db_snapshot_attribute_list.serialize_query(
            value["db_snapshot_attributes"], pairs, f"{prefix}.DBSnapshotAttributes"
        )


def deserialize_query(el: Element) -> DBSnapshotAttributesResult:
    out: DBSnapshotAttributesResult = {}  # type: ignore[typeddict-item]
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_db_snapshot_attributes = el.find("DBSnapshotAttributes")
    if child_db_snapshot_attributes is not None:
        import aws_sdk_rds.types.db_snapshot_attribute_list

        out["db_snapshot_attributes"] = (
            aws_sdk_rds.types.db_snapshot_attribute_list.deserialize_query(
                child_db_snapshot_attributes
            )
        )
    return out
