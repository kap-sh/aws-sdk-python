"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetSandboxesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.sandbox_ids
    import aws_sdk_codebuild.types.sandboxes


class BatchGetSandboxesOutput(TypedDict):
    sandboxes: NotRequired["aws_sdk_codebuild.types.sandboxes.Sandboxes"]
    """<p>Information about the requested sandboxes.</p>"""
    sandboxes_not_found: NotRequired["aws_sdk_codebuild.types.sandbox_ids.SandboxIds"]
    """<p>The IDs of sandboxes for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetSandboxesOutput) -> dict:
    out: dict = {}
    if "sandboxes" in value:
        import aws_sdk_codebuild.types.sandboxes

        out["sandboxes"] = aws_sdk_codebuild.types.sandboxes.serialize_aws_json_1_1(
            value["sandboxes"]
        )
    if "sandboxes_not_found" in value:
        import aws_sdk_codebuild.types.sandbox_ids

        out["sandboxesNotFound"] = (
            aws_sdk_codebuild.types.sandbox_ids.serialize_aws_json_1_1(
                value["sandboxes_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetSandboxesOutput:
    out: BatchGetSandboxesOutput = {}  # type: ignore[typeddict-item]
    if "sandboxes" in data:
        import aws_sdk_codebuild.types.sandboxes

        out["sandboxes"] = aws_sdk_codebuild.types.sandboxes.deserialize_aws_json_1_1(
            data["sandboxes"]
        )
    if "sandboxesNotFound" in data:
        import aws_sdk_codebuild.types.sandbox_ids

        out["sandboxes_not_found"] = (
            aws_sdk_codebuild.types.sandbox_ids.deserialize_aws_json_1_1(
                data["sandboxesNotFound"]
            )
        )
    return out
