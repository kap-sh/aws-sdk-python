"""Generated from Smithy shape ``com.amazonaws.codepipeline#RetryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.stage_retry_mode


class RetryConfiguration(TypedDict):
    retry_mode: NotRequired[
        "aws_sdk_codepipeline.types.stage_retry_mode.StageRetryMode"
    ]
    """<p>The method that you want to configure for automatic stage retry on stage failure. You can specify to retry only failed action in the stage or all actions in the stage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryConfiguration) -> dict:
    out: dict = {}
    if "retry_mode" in value:
        import aws_sdk_codepipeline.types.stage_retry_mode

        out["retryMode"] = (
            aws_sdk_codepipeline.types.stage_retry_mode.serialize_aws_json_1_1(
                value["retry_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryConfiguration:
    out: RetryConfiguration = {}  # type: ignore[typeddict-item]
    if "retryMode" in data:
        import aws_sdk_codepipeline.types.stage_retry_mode

        out["retry_mode"] = (
            aws_sdk_codepipeline.types.stage_retry_mode.deserialize_aws_json_1_1(
                data["retryMode"]
            )
        )
    return out
