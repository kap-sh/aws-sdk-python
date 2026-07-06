"""Generated from Smithy shape ``com.amazonaws.neptune#ListTagsForResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.filter_list
    import aws_sdk_neptune.types.string


class ListTagsForResourceMessage(TypedDict, closed=True):
    resource_name: NotRequired["aws_sdk_neptune.types.string.String"]
    r"""<p>The Amazon Neptune resource with tags to be listed. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href=\"https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing\"> Constructing an Amazon Resource Name (ARN)</a>.</p>"""
    filters: NotRequired["aws_sdk_neptune.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTagsForResourceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_name" in value:
        pairs.append((f"{prefix}.ResourceName", str(value["resource_name"])))
    if "filters" in value:
        import aws_sdk_neptune.types.filter_list

        aws_sdk_neptune.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_query(el: Element) -> ListTagsForResourceMessage:
    out: ListTagsForResourceMessage = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_neptune.types.filter_list

        out["filters"] = aws_sdk_neptune.types.filter_list.deserialize_query(
            child_filters
        )
    return out
