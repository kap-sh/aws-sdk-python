"""Generated from Smithy shape ``com.amazonaws.neptune#CreateDBParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string
    import capo_neptune.types.tag_list


class CreateDBParameterGroupMessage(TypedDict, closed=True):
    db_parameter_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <note> <p>This value is stored as a lowercase string.</p> </note>"""
    db_parameter_group_family: NotRequired["capo_neptune.types.string.String"]
    """<p>The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.</p>"""
    description: NotRequired["capo_neptune.types.string.String"]
    """<p>The description for the DB parameter group.</p>"""
    tags: NotRequired["capo_neptune.types.tag_list.TagList"]
    """<p>The tags to be assigned to the new DB parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBParameterGroupName", str(value["db_parameter_group_name"]))
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
        import capo_neptune.types.tag_list

        capo_neptune.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateDBParameterGroupMessage:
    out: CreateDBParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
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
        import capo_neptune.types.tag_list

        out["tags"] = capo_neptune.types.tag_list.deserialize_query(child_tags)
    return out
