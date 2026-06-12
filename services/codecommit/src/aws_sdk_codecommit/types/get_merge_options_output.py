"""Generated from Smithy shape ``com.amazonaws.codecommit#GetMergeOptionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.merge_options
    import aws_sdk_codecommit.types.object_id


class GetMergeOptionsOutput(TypedDict):
    merge_options: "aws_sdk_codecommit.types.merge_options.MergeOptions"
    """<p>The merge option or strategy used to merge the code.</p>"""
    source_commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the source commit specifier that was used in the merge evaluation.</p>"""
    destination_commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the destination commit specifier that was used in the merge evaluation.</p>"""
    base_commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the merge base.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMergeOptionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.merge_options

    out["mergeOptions"] = aws_sdk_codecommit.types.merge_options.serialize_aws_json_1_1(
        value["merge_options"]
    )
    out["sourceCommitId"] = value["source_commit_id"]
    out["destinationCommitId"] = value["destination_commit_id"]
    out["baseCommitId"] = value["base_commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMergeOptionsOutput:
    out: GetMergeOptionsOutput = {}  # type: ignore[typeddict-item]
    if "mergeOptions" in data:
        import aws_sdk_codecommit.types.merge_options

        out["merge_options"] = (
            aws_sdk_codecommit.types.merge_options.deserialize_aws_json_1_1(
                data["mergeOptions"]
            )
        )
    else:
        raise DeserializationError("GetMergeOptionsOutput.merge_options required")
    if "sourceCommitId" in data:
        out["source_commit_id"] = data["sourceCommitId"]
    else:
        raise DeserializationError("GetMergeOptionsOutput.source_commit_id required")
    if "destinationCommitId" in data:
        out["destination_commit_id"] = data["destinationCommitId"]
    else:
        raise DeserializationError(
            "GetMergeOptionsOutput.destination_commit_id required"
        )
    if "baseCommitId" in data:
        out["base_commit_id"] = data["baseCommitId"]
    else:
        raise DeserializationError("GetMergeOptionsOutput.base_commit_id required")
    return out
