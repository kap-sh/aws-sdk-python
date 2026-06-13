"""Generated from Smithy shape ``com.amazonaws.bedrock#TrainingDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.invocation_logs_config
    import aws_sdk_bedrock.types.s3_uri


class TrainingDataConfig(TypedDict):
    s3_uri: NotRequired["aws_sdk_bedrock.types.s3_uri.S3Uri"]
    """<p>The S3 URI where the training data is stored.</p>"""
    invocation_logs_config: NotRequired[
        "aws_sdk_bedrock.types.invocation_logs_config.InvocationLogsConfig"
    ]
    """<p>Settings for using invocation logs to customize a model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainingDataConfig) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["s3Uri"] = value["s3_uri"]
    if "invocation_logs_config" in value:
        import aws_sdk_bedrock.types.invocation_logs_config

        out["invocationLogsConfig"] = (
            aws_sdk_bedrock.types.invocation_logs_config.serialize_json(
                value["invocation_logs_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrainingDataConfig:
    out: TrainingDataConfig = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    if "invocationLogsConfig" in data:
        import aws_sdk_bedrock.types.invocation_logs_config

        out["invocation_logs_config"] = (
            aws_sdk_bedrock.types.invocation_logs_config.deserialize_json(
                data["invocationLogsConfig"]
            )
        )
    return out
