"""Generated from Smithy shape ``com.amazonaws.docdb#CreateDBClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string
    import capo_docdb.types.tag_list


class CreateDBClusterParameterGroupMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must not match the name of an existing <code>DBClusterParameterGroup</code>.</p> </li> </ul> <note> <p>This value is stored as a lowercase string.</p> </note>"""
    db_parameter_group_family: NotRequired["capo_docdb.types.string.String"]
    """<p>The cluster parameter group family name.</p>"""
    description: NotRequired["capo_docdb.types.string.String"]
    """<p>The description for the cluster parameter group.</p>"""
    tags: NotRequired["capo_docdb.types.tag_list.TagList"]
    """<p>The tags to be assigned to the cluster parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterParameterGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{key_prefix}DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tags" in value:
        import capo_docdb.types.tag_list

        capo_docdb.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateDBClusterParameterGroupMessage:
    out: CreateDBClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_docdb.types.tag_list

        out["tags"] = capo_docdb.types.tag_list.deserialize_query(child_tags)
    return out
