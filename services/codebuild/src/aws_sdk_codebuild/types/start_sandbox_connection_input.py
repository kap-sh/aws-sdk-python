"""Generated from Smithy shape ``com.amazonaws.codebuild#StartSandboxConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class StartSandboxConnectionInput(TypedDict):
    sandbox_id: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSandboxConnectionInput) -> dict:
    out: dict = {}
    out["sandboxId"] = value["sandbox_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSandboxConnectionInput:
    out: StartSandboxConnectionInput = {}  # type: ignore[typeddict-item]
    if "sandboxId" in data:
        out["sandbox_id"] = data["sandboxId"]
    else:
        raise DeserializationError("StartSandboxConnectionInput.sandbox_id required")
    return out
