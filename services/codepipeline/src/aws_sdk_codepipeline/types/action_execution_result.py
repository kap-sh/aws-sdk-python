"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecutionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.error_details
    import aws_sdk_codepipeline.types.external_execution_id
    import aws_sdk_codepipeline.types.external_execution_summary
    import aws_sdk_codepipeline.types.log_stream_arn
    import aws_sdk_codepipeline.types.url


class ActionExecutionResult(TypedDict):
    external_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.external_execution_id.ExternalExecutionId"
    ]
    """<p>The action provider's external ID for the action execution.</p>"""
    external_execution_summary: NotRequired[
        "aws_sdk_codepipeline.types.external_execution_summary.ExternalExecutionSummary"
    ]
    """<p>The action provider's summary for the action execution.</p>"""
    external_execution_url: NotRequired["aws_sdk_codepipeline.types.url.Url"]
    """<p>The deepest external link to the external resource (for example, a repository URL or deployment endpoint) that is used when running the action.</p>"""
    error_details: NotRequired["aws_sdk_codepipeline.types.error_details.ErrorDetails"]
    log_stream_arn: NotRequired[
        "aws_sdk_codepipeline.types.log_stream_arn.LogStreamARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the log stream for the action compute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecutionResult) -> dict:
    out: dict = {}
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "external_execution_summary" in value:
        out["externalExecutionSummary"] = value["external_execution_summary"]
    if "external_execution_url" in value:
        out["externalExecutionUrl"] = value["external_execution_url"]
    if "error_details" in value:
        import aws_sdk_codepipeline.types.error_details

        out["errorDetails"] = (
            aws_sdk_codepipeline.types.error_details.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    if "log_stream_arn" in value:
        out["logStreamARN"] = value["log_stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionExecutionResult:
    out: ActionExecutionResult = {}  # type: ignore[typeddict-item]
    if "externalExecutionId" in data:
        out["external_execution_id"] = data["externalExecutionId"]
    if "externalExecutionSummary" in data:
        out["external_execution_summary"] = data["externalExecutionSummary"]
    if "externalExecutionUrl" in data:
        out["external_execution_url"] = data["externalExecutionUrl"]
    if "errorDetails" in data:
        import aws_sdk_codepipeline.types.error_details

        out["error_details"] = (
            aws_sdk_codepipeline.types.error_details.deserialize_aws_json_1_1(
                data["errorDetails"]
            )
        )
    if "logStreamARN" in data:
        out["log_stream_arn"] = data["logStreamARN"]
    return out
