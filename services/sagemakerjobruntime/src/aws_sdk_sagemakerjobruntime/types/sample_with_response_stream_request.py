"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#SampleWithResponseStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemakerjobruntime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemakerjobruntime.types.inference_request_body
    import aws_sdk_sagemakerjobruntime.types.job_arn
    import aws_sdk_sagemakerjobruntime.types.trajectory_id


class SampleWithResponseStreamRequest(TypedDict):
    job_arn: "aws_sdk_sagemakerjobruntime.types.job_arn.JobArn"
    """The job ARN that identifies which model session to route the inference request to."""
    trajectory_id: "aws_sdk_sagemakerjobruntime.types.trajectory_id.TrajectoryId"
    """The trajectory ID for grouping turns into a single rollout. Each turn is captured for later use."""
    body: (
        "aws_sdk_sagemakerjobruntime.types.inference_request_body.InferenceRequestBody"
    )
    """The raw inference request body in OpenAI-compatible JSON format."""


# --- restJson1 ser/de ---
def serialize_json(value: SampleWithResponseStreamRequest) -> dict:
    out: dict = {}
    import aws_sdk_sagemakerjobruntime.types.inference_request_body

    out["Body"] = (
        aws_sdk_sagemakerjobruntime.types.inference_request_body.serialize_json(
            value["body"]
        )
    )
    return out


def deserialize_json(data: dict) -> SampleWithResponseStreamRequest:
    out: SampleWithResponseStreamRequest = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        import aws_sdk_sagemakerjobruntime.types.inference_request_body

        out["body"] = (
            aws_sdk_sagemakerjobruntime.types.inference_request_body.deserialize_json(
                data["Body"]
            )
        )
    else:
        raise DeserializationError("SampleWithResponseStreamRequest.body required")
    return out
