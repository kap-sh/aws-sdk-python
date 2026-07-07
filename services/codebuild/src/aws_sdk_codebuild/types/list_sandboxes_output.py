"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSandboxesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.sandbox_ids
    import aws_sdk_codebuild.types.string


class ListSandboxesOutput(TypedDict, closed=True):
    ids: NotRequired["aws_sdk_codebuild.types.sandbox_ids.SandboxIds"]
    """<p>Information about the requested sandbox IDs.</p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>Information about the next token to get paginated results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSandboxesOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_codebuild.types.sandbox_ids

        out["ids"] = aws_sdk_codebuild.types.sandbox_ids.serialize_aws_json_1_1(
            value["ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSandboxesOutput:
    out: ListSandboxesOutput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_codebuild.types.sandbox_ids

        out["ids"] = aws_sdk_codebuild.types.sandbox_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
