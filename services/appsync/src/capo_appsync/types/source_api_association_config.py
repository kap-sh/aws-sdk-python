"""Generated from Smithy shape ``com.amazonaws.appsync#SourceApiAssociationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.merge_type


class SourceApiAssociationConfig(TypedDict, closed=True):
    merge_type: NotRequired["capo_appsync.types.merge_type.MergeType"]
    """<p>The property that indicates which merging option is enabled in the source API association.</p> <p>Valid merge types are <code>MANUAL_MERGE</code> (default) and <code>AUTO_MERGE</code>. Manual merges are the default behavior and require the user to trigger any changes from the source APIs to the merged API manually. Auto merges subscribe the merged API to the changes performed on the source APIs so that any change in the source APIs are also made to the merged API. Auto merges use <code>MergedApiExecutionRoleArn</code> to perform merge operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceApiAssociationConfig) -> dict:
    out: dict = {}
    if "merge_type" in value:
        import capo_appsync.types.merge_type

        out["mergeType"] = capo_appsync.types.merge_type.serialize_json(
            value["merge_type"]
        )
    return out


def deserialize_json(data: dict) -> SourceApiAssociationConfig:
    out: SourceApiAssociationConfig = {}  # type: ignore[typeddict-item]
    if "mergeType" in data:
        import capo_appsync.types.merge_type

        out["merge_type"] = capo_appsync.types.merge_type.deserialize_json(
            data["mergeType"]
        )
    return out
