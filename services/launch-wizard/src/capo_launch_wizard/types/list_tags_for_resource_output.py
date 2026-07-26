"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.tags


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_launch_wizard.types.tags.Tags"]
    """<p>Information about the tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_launch_wizard.types.tags

        out["tags"] = capo_launch_wizard.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_launch_wizard.types.tags

        out["tags"] = capo_launch_wizard.types.tags.deserialize_json(data["tags"])
    return out
