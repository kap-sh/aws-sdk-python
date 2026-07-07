"""Generated from Smithy shape ``com.amazonaws.codebuild#ListBuildBatchesForProjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_batch_ids
    import aws_sdk_codebuild.types.string


class ListBuildBatchesForProjectOutput(TypedDict, closed=True):
    ids: NotRequired["aws_sdk_codebuild.types.build_batch_ids.BuildBatchIds"]
    """<p>An array of strings that contains the batch build identifiers.</p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to <code>ListBuildBatchesForProject</code> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildBatchesForProjectOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_codebuild.types.build_batch_ids

        out["ids"] = aws_sdk_codebuild.types.build_batch_ids.serialize_aws_json_1_1(
            value["ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildBatchesForProjectOutput:
    out: ListBuildBatchesForProjectOutput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_codebuild.types.build_batch_ids

        out["ids"] = aws_sdk_codebuild.types.build_batch_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
