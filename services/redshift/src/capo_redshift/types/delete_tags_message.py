"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteTagsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.tag_key_list


class DeleteTagsMessage(TypedDict, closed=True):
    resource_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, <code>arn:aws:redshift:us-east-2:123456789:cluster:t1</code>. </p>"""
    tag_keys: NotRequired["capo_redshift.types.tag_key_list.TagKeyList"]
    """<p>The tag key that you want to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTagsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_name" in value:
        pairs.append((f"{key_prefix}ResourceName", str(value["resource_name"])))
    if "tag_keys" in value:
        import capo_redshift.types.tag_key_list

        capo_redshift.types.tag_key_list.serialize_query(
            value["tag_keys"], pairs, f"{key_prefix}TagKeys"
        )


def deserialize_query(el: Element) -> DeleteTagsMessage:
    out: DeleteTagsMessage = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_redshift.types.tag_key_list

        out["tag_keys"] = capo_redshift.types.tag_key_list.deserialize_query(
            child_tag_keys
        )
    return out
