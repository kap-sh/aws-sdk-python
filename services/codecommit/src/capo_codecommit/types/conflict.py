"""Generated from Smithy shape ``com.amazonaws.codecommit#Conflict``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.conflict_metadata
    import capo_codecommit.types.merge_hunks


class Conflict(TypedDict, closed=True):
    conflict_metadata: NotRequired[
        "capo_codecommit.types.conflict_metadata.ConflictMetadata"
    ]
    """<p>Metadata about a conflict in a merge operation.</p>"""
    merge_hunks: NotRequired["capo_codecommit.types.merge_hunks.MergeHunks"]
    """<p>A list of hunks that contain the differences between files or lines causing the conflict.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Conflict) -> dict:
    out: dict = {}
    if "conflict_metadata" in value:
        import capo_codecommit.types.conflict_metadata

        out["conflictMetadata"] = (
            capo_codecommit.types.conflict_metadata.serialize_aws_json_1_1(
                value["conflict_metadata"]
            )
        )
    if "merge_hunks" in value:
        import capo_codecommit.types.merge_hunks

        out["mergeHunks"] = capo_codecommit.types.merge_hunks.serialize_aws_json_1_1(
            value["merge_hunks"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Conflict:
    out: Conflict = {}  # type: ignore[typeddict-item]
    if "conflictMetadata" in data:
        import capo_codecommit.types.conflict_metadata

        out["conflict_metadata"] = (
            capo_codecommit.types.conflict_metadata.deserialize_aws_json_1_1(
                data["conflictMetadata"]
            )
        )
    if "mergeHunks" in data:
        import capo_codecommit.types.merge_hunks

        out["merge_hunks"] = capo_codecommit.types.merge_hunks.deserialize_aws_json_1_1(
            data["mergeHunks"]
        )
    return out
