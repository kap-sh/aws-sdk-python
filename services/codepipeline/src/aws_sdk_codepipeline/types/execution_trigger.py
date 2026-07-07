"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutionTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.trigger_detail
    import aws_sdk_codepipeline.types.trigger_type


class ExecutionTrigger(TypedDict, closed=True):
    trigger_type: NotRequired["aws_sdk_codepipeline.types.trigger_type.TriggerType"]
    """<p>The type of change-detection method, command, or user interaction that started a pipeline execution.</p>"""
    trigger_detail: NotRequired[
        "aws_sdk_codepipeline.types.trigger_detail.TriggerDetail"
    ]
    """<p>Detail related to the event that started a pipeline execution, such as the webhook ARN of the webhook that triggered the pipeline execution or the user ARN for a user-initiated <code>start-pipeline-execution</code> CLI command.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionTrigger) -> dict:
    out: dict = {}
    if "trigger_type" in value:
        import aws_sdk_codepipeline.types.trigger_type

        out["triggerType"] = (
            aws_sdk_codepipeline.types.trigger_type.serialize_aws_json_1_1(
                value["trigger_type"]
            )
        )
    if "trigger_detail" in value:
        out["triggerDetail"] = value["trigger_detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionTrigger:
    out: ExecutionTrigger = {}  # type: ignore[typeddict-item]
    if "triggerType" in data:
        import aws_sdk_codepipeline.types.trigger_type

        out["trigger_type"] = (
            aws_sdk_codepipeline.types.trigger_type.deserialize_aws_json_1_1(
                data["triggerType"]
            )
        )
    if "triggerDetail" in data:
        out["trigger_detail"] = data["triggerDetail"]
    return out
