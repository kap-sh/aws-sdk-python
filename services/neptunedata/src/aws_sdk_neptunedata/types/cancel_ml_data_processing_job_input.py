"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelMLDataProcessingJobInput``."""

from typing import TypedDict
from typing_extensions import NotRequired

class CancelMLDataProcessingJobInput(TypedDict):
    id: "str"
    """<p>The unique identifier of the data-processing job.</p>"""
    neptune_iam_role_arn: NotRequired["str"]
    """<p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>"""
    clean: NotRequired["bool"]
    """<p>If set to <code>TRUE</code>, this flag specifies that all Neptune ML S3 artifacts should be deleted when the job is stopped. The default is <code>FALSE</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CancelMLDataProcessingJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelMLDataProcessingJobInput:
    out: CancelMLDataProcessingJobInput = {}  # type: ignore[typeddict-item]
    return out