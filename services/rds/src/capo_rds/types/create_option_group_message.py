"""Generated from Smithy shape ``com.amazonaws.rds#CreateOptionGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CreateOptionGroupMessage(TypedDict, closed=True):
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the option group to be created.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>myoptiongroup</code> </p>"""
    engine_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the engine to associate this option group with.</p> <p>Valid Values:</p> <ul> <li> <p> <code>db2-ae</code> </p> </li> <li> <p> <code>db2-se</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>"""
    major_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the major version of the engine that this option group should be associated with.</p>"""
    option_group_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description of the option group.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the option group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateOptionGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "engine_name" in value:
        pairs.append((f"{key_prefix}EngineName", str(value["engine_name"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "option_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}OptionGroupDescription",
                str(value["option_group_description"]),
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateOptionGroupMessage:
    out: CreateOptionGroupMessage = {}  # type: ignore[typeddict-item]
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_engine_name = el.find("EngineName")
    if child_engine_name is not None:
        out["engine_name"] = str(child_engine_name.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    child_option_group_description = el.find("OptionGroupDescription")
    if child_option_group_description is not None:
        out["option_group_description"] = str(child_option_group_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
