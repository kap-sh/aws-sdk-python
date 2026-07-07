"""Generated from Smithy shape ``com.amazonaws.neptune#AddTagsToResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string
    import aws_sdk_neptune.types.tag_list


class AddTagsToResourceMessage(TypedDict, closed=True):
    resource_name: NotRequired["aws_sdk_neptune.types.string.String"]
    r"""<p>The Amazon Neptune resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href=\"https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing\"> Constructing an Amazon Resource Name (ARN)</a>.</p>"""
    tags: NotRequired["aws_sdk_neptune.types.tag_list.TagList"]
    """<p>The tags to be assigned to the Amazon Neptune resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddTagsToResourceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_name" in value:
        pairs.append((f"{prefix}.ResourceName", str(value["resource_name"])))
    if "tags" in value:
        import aws_sdk_neptune.types.tag_list

        aws_sdk_neptune.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> AddTagsToResourceMessage:
    out: AddTagsToResourceMessage = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_neptune.types.tag_list

        out["tags"] = aws_sdk_neptune.types.tag_list.deserialize_query(child_tags)
    return out
