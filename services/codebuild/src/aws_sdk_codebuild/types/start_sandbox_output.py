"""Generated from Smithy shape ``com.amazonaws.codebuild#StartSandboxOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.sandbox


class StartSandboxOutput(TypedDict, closed=True):
    sandbox: NotRequired["aws_sdk_codebuild.types.sandbox.Sandbox"]
    """<p>Information about the requested sandbox.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSandboxOutput) -> dict:
    out: dict = {}
    if "sandbox" in value:
        import aws_sdk_codebuild.types.sandbox

        out["sandbox"] = aws_sdk_codebuild.types.sandbox.serialize_aws_json_1_1(
            value["sandbox"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSandboxOutput:
    out: StartSandboxOutput = {}  # type: ignore[typeddict-item]
    if "sandbox" in data:
        import aws_sdk_codebuild.types.sandbox

        out["sandbox"] = aws_sdk_codebuild.types.sandbox.deserialize_aws_json_1_1(
            data["sandbox"]
        )
    return out
