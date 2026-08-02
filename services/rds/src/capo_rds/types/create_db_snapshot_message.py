"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CreateDBSnapshotMessage(TypedDict, closed=True):
    db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the DB snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Can't be null, empty, or blank</p> </li> <li> <p>Must contain from 1 to 255 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-snapshot-id</code> </p>"""
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the DB instance that you want to create the snapshot of.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBInstance.</p> </li> </ul>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateDBSnapshotMessage:
    out: CreateDBSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
