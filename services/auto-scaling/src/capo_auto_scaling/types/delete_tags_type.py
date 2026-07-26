"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeleteTagsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.tags


class DeleteTagsType(TypedDict, closed=True):
    tags: NotRequired["capo_auto_scaling.types.tags.Tags"]
    """<p>One or more tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTagsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tags" in value:
        import capo_auto_scaling.types.tags

        capo_auto_scaling.types.tags.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> DeleteTagsType:
    out: DeleteTagsType = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_auto_scaling.types.tags

        out["tags"] = capo_auto_scaling.types.tags.deserialize_query(child_tags)
    return out
