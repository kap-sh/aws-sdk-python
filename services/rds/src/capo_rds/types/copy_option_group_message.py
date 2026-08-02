"""Generated from Smithy shape ``com.amazonaws.rds#CopyOptionGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CopyOptionGroupMessage(TypedDict, closed=True):
    source_option_group_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the source option group.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid option group.</p> </li> </ul>"""
    target_option_group_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the copied option group.</p> <p>Constraints:</p> <ul> <li> <p>Can't be null, empty, or blank</p> </li> <li> <p>Must contain from 1 to 255 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-option-group</code> </p>"""
    target_option_group_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description for the copied option group.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyOptionGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_option_group_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceOptionGroupIdentifier",
                str(value["source_option_group_identifier"]),
            )
        )
    if "target_option_group_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}TargetOptionGroupIdentifier",
                str(value["target_option_group_identifier"]),
            )
        )
    if "target_option_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}TargetOptionGroupDescription",
                str(value["target_option_group_description"]),
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CopyOptionGroupMessage:
    out: CopyOptionGroupMessage = {}  # type: ignore[typeddict-item]
    child_source_option_group_identifier = el.find("SourceOptionGroupIdentifier")
    if child_source_option_group_identifier is not None:
        out["source_option_group_identifier"] = str(
            child_source_option_group_identifier.text or ""
        )
    child_target_option_group_identifier = el.find("TargetOptionGroupIdentifier")
    if child_target_option_group_identifier is not None:
        out["target_option_group_identifier"] = str(
            child_target_option_group_identifier.text or ""
        )
    child_target_option_group_description = el.find("TargetOptionGroupDescription")
    if child_target_option_group_description is not None:
        out["target_option_group_description"] = str(
            child_target_option_group_description.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
