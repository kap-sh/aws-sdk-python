"""Generated from Smithy shape ``com.amazonaws.tnb#CreateSolFunctionPackageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.tag_map


class CreateSolFunctionPackageInput(TypedDict, closed=True):
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSolFunctionPackageInput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSolFunctionPackageInput:
    out: CreateSolFunctionPackageInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
