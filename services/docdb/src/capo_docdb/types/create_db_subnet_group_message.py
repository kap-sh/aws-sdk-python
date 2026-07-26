"""Generated from Smithy shape ``com.amazonaws.docdb#CreateDBSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string
    import capo_docdb.types.subnet_identifier_list
    import capo_docdb.types.tag_list


class CreateDBSubnetGroupMessage(TypedDict, closed=True):
    db_subnet_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The name for the subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>"""
    db_subnet_group_description: NotRequired["capo_docdb.types.string.String"]
    """<p>The description for the subnet group.</p>"""
    subnet_ids: NotRequired[
        "capo_docdb.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>The Amazon EC2 subnet IDs for the subnet group.</p>"""
    tags: NotRequired["capo_docdb.types.tag_list.TagList"]
    """<p>The tags to be assigned to the subnet group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{prefix}.DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "db_subnet_group_description" in value:
        pairs.append(
            (
                f"{prefix}.DBSubnetGroupDescription",
                str(value["db_subnet_group_description"]),
            )
        )
    if "subnet_ids" in value:
        import capo_docdb.types.subnet_identifier_list

        capo_docdb.types.subnet_identifier_list.serialize_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "tags" in value:
        import capo_docdb.types.tag_list

        capo_docdb.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
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
        import capo_docdb.types.subnet_identifier_list

        out["subnet_ids"] = capo_docdb.types.subnet_identifier_list.deserialize_query(
            child_subnet_ids
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_docdb.types.tag_list

        out["tags"] = capo_docdb.types.tag_list.deserialize_query(child_tags)
    return out
