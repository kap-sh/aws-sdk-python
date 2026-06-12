"""Generated from Smithy shape ``com.amazonaws.codebuild#StartSandboxInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.sensitive_string


class StartSandboxInput(TypedDict):
    project_name: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The CodeBuild project name.</p>"""
    idempotency_token: NotRequired[
        "aws_sdk_codebuild.types.sensitive_string.SensitiveString"
    ]
    """<p>A unique client token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSandboxInput) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSandboxInput:
    out: StartSandboxInput = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    if "idempotencyToken" in data:
        out["idempotency_token"] = data["idempotencyToken"]
    return out
