"""Generated from Smithy shape ``com.amazonaws.neptunedata#DeleteMLEndpointInput``."""

from typing_extensions import NotRequired, TypedDict


class DeleteMLEndpointInput(TypedDict, closed=True):
    id: "str"
    """<p>The unique identifier of the inference endpoint.</p>"""
    neptune_iam_role_arn: NotRequired["str"]
    """<p>The ARN of an IAM role providing Neptune access to SageMaker and Amazon S3 resources. This must be listed in your DB cluster parameter group or an error will be thrown.</p>"""
    clean: NotRequired["bool"]
    """<p>If this flag is set to <code>TRUE</code>, all Neptune ML S3 artifacts should be deleted when the job is stopped. The default is <code>FALSE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMLEndpointInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMLEndpointInput:
    out: DeleteMLEndpointInput = {}  # type: ignore[typeddict-item]
    return out
