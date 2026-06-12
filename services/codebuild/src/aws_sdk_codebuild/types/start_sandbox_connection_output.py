"""Generated from Smithy shape ``com.amazonaws.codebuild#StartSandboxConnectionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.ssm_session


class StartSandboxConnectionOutput(TypedDict):
    ssm_session: NotRequired["aws_sdk_codebuild.types.ssm_session.SSMSession"]
    """<p>Information about the Session Manager session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSandboxConnectionOutput) -> dict:
    out: dict = {}
    if "ssm_session" in value:
        import aws_sdk_codebuild.types.ssm_session

        out["ssmSession"] = aws_sdk_codebuild.types.ssm_session.serialize_aws_json_1_1(
            value["ssm_session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSandboxConnectionOutput:
    out: StartSandboxConnectionOutput = {}  # type: ignore[typeddict-item]
    if "ssmSession" in data:
        import aws_sdk_codebuild.types.ssm_session

        out["ssm_session"] = (
            aws_sdk_codebuild.types.ssm_session.deserialize_aws_json_1_1(
                data["ssmSession"]
            )
        )
    return out
