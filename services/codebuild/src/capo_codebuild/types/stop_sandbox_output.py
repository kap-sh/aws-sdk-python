"""Generated from Smithy shape ``com.amazonaws.codebuild#StopSandboxOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.sandbox


class StopSandboxOutput(TypedDict, closed=True):
    sandbox: NotRequired["capo_codebuild.types.sandbox.Sandbox"]
    """<p>Information about the requested sandbox.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSandboxOutput) -> dict:
    out: dict = {}
    if "sandbox" in value:
        import capo_codebuild.types.sandbox

        out["sandbox"] = capo_codebuild.types.sandbox.serialize_aws_json_1_1(
            value["sandbox"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSandboxOutput:
    out: StopSandboxOutput = {}  # type: ignore[typeddict-item]
    if "sandbox" in data:
        import capo_codebuild.types.sandbox

        out["sandbox"] = capo_codebuild.types.sandbox.deserialize_aws_json_1_1(
            data["sandbox"]
        )
    return out
