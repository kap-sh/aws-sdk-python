"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetMLEndpointInput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GetMLEndpointInput(TypedDict):
    id: "str"
    """<p>The unique identifier of the inference endpoint.</p>"""
    neptune_iam_role_arn: NotRequired["str"]
    """<p>The ARN of an IAM role that provides Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLEndpointInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMLEndpointInput:
    out: GetMLEndpointInput = {}  # type: ignore[typeddict-item]
    return out
