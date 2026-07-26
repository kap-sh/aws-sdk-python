"""Generated from Smithy shape ``com.amazonaws.mgn#MergeOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.merge_constructs


class MergeOperation(TypedDict, closed=True):
    merge_constructs: NotRequired["capo_mgn.types.merge_constructs.MergeConstructs"]
    """<p>The list of constructs to merge into the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MergeOperation) -> dict:
    out: dict = {}
    if "merge_constructs" in value:
        import capo_mgn.types.merge_constructs

        out["mergeConstructs"] = capo_mgn.types.merge_constructs.serialize_json(
            value["merge_constructs"]
        )
    return out


def deserialize_json(data: dict) -> MergeOperation:
    out: MergeOperation = {}  # type: ignore[typeddict-item]
    if "mergeConstructs" in data:
        import capo_mgn.types.merge_constructs

        out["merge_constructs"] = capo_mgn.types.merge_constructs.deserialize_json(
            data["mergeConstructs"]
        )
    return out
