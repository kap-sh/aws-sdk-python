"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.subnet_identifier_list
    import capo_rds.types.tag_list


class CreateDBSubnetGroupMessage(TypedDict, closed=True):
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name for the DB subnet group. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens.</p> </li> <li> <p>Must not be default.</p> </li> <li> <p>First character must be a letter.</p> </li> </ul> <p>Example: <code>mydbsubnetgroup</code> </p>"""
    db_subnet_group_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description for the DB subnet group.</p>"""
    subnet_ids: NotRequired[
        "capo_rds.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>The EC2 Subnet IDs for the DB subnet group.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the DB subnet group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "db_subnet_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}DBSubnetGroupDescription",
                str(value["db_subnet_group_description"]),
            )
        )
    if "subnet_ids" in value:
        import capo_rds.types.subnet_identifier_list

        capo_rds.types.subnet_identifier_list.serialize_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetIds"
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateDBSubnetGroupMessage:
    out: CreateDBSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_db_subnet_group_description = el.find("DBSubnetGroupDescription")
    if child_db_subnet_group_description is not None:
        out["db_subnet_group_description"] = str(
            child_db_subnet_group_description.text or ""
        )
    child_subnet_ids = el.find("SubnetIds")
    if child_subnet_ids is not None:
        import capo_rds.types.subnet_identifier_list

        out["subnet_ids"] = capo_rds.types.subnet_identifier_list.deserialize_query(
            child_subnet_ids
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
