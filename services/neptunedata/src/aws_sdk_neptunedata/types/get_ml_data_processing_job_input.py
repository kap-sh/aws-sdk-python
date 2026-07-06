"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetMLDataProcessingJobInput``."""

from typing_extensions import NotRequired, TypedDict


class GetMLDataProcessingJobInput(TypedDict, closed=True):
    id: "str"
    """<p>The unique identifier of the data-processing job to be retrieved.</p>"""
    neptune_iam_role_arn: NotRequired["str"]
    """<p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLDataProcessingJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMLDataProcessingJobInput:
    out: GetMLDataProcessingJobInput = {}  # type: ignore[typeddict-item]
    return out
