"""Generated from Smithy shape ``com.amazonaws.codebuild#ListBuildsForProjectOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_ids
    import aws_sdk_codebuild.types.string


class ListBuildsForProjectOutput(TypedDict):
    ids: NotRequired["aws_sdk_codebuild.types.build_ids.BuildIds"]
    """<p>A list of build identifiers for the specified build project, with each build ID representing a single build.</p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildsForProjectOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_codebuild.types.build_ids

        out["ids"] = aws_sdk_codebuild.types.build_ids.serialize_aws_json_1_1(
            value["ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildsForProjectOutput:
    out: ListBuildsForProjectOutput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_codebuild.types.build_ids

        out["ids"] = aws_sdk_codebuild.types.build_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
