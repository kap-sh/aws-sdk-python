"""Generated from Smithy shape ``com.amazonaws.mgn#MergeOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.merge_constructs


class MergeOperation(TypedDict):
    merge_constructs: NotRequired["aws_sdk_mgn.types.merge_constructs.MergeConstructs"]
    """<p>The list of constructs to merge into the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MergeOperation) -> dict:
    out: dict = {}
    if "merge_constructs" in value:
        import aws_sdk_mgn.types.merge_constructs

        out["mergeConstructs"] = aws_sdk_mgn.types.merge_constructs.serialize_json(
            value["merge_constructs"]
        )
    return out


def deserialize_json(data: dict) -> MergeOperation:
    out: MergeOperation = {}  # type: ignore[typeddict-item]
    if "mergeConstructs" in data:
        import aws_sdk_mgn.types.merge_constructs

        out["merge_constructs"] = aws_sdk_mgn.types.merge_constructs.deserialize_json(
            data["mergeConstructs"]
        )
    return out
