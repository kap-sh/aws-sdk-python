"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetSandboxesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.sandbox_ids


class BatchGetSandboxesInput(TypedDict):
    ids: "aws_sdk_codebuild.types.sandbox_ids.SandboxIds"
    """<p>A comma separated list of <code>sandboxIds</code> or <code>sandboxArns</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetSandboxesInput) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.sandbox_ids

    out["ids"] = aws_sdk_codebuild.types.sandbox_ids.serialize_aws_json_1_1(
        value["ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetSandboxesInput:
    out: BatchGetSandboxesInput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_codebuild.types.sandbox_ids

        out["ids"] = aws_sdk_codebuild.types.sandbox_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    else:
        raise DeserializationError("BatchGetSandboxesInput.ids required")
    return out
