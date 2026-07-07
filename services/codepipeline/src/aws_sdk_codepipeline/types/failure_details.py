"""Generated from Smithy shape ``com.amazonaws.codepipeline#FailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.execution_id
    import aws_sdk_codepipeline.types.failure_type
    import aws_sdk_codepipeline.types.message


class FailureDetails(TypedDict, closed=True):
    type: "aws_sdk_codepipeline.types.failure_type.FailureType"
    """<p>The type of the failure.</p>"""
    message: "aws_sdk_codepipeline.types.message.Message"
    """<p>The message about the failure.</p>"""
    external_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.execution_id.ExecutionId"
    ]
    """<p>The external ID of the run of the action that failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureDetails) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.failure_type

    out["type"] = aws_sdk_codepipeline.types.failure_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["message"] = value["message"]
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureDetails:
    out: FailureDetails = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_codepipeline.types.failure_type

        out["type"] = aws_sdk_codepipeline.types.failure_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("FailureDetails.type required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("FailureDetails.message required")
    if "externalExecutionId" in data:
        out["external_execution_id"] = data["externalExecutionId"]
    return out
