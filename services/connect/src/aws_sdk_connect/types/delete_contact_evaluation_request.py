"""Generated from Smithy shape ``com.amazonaws.connect#DeleteContactEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.resource_id


class DeleteContactEvaluationRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    evaluation_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContactEvaluationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContactEvaluationRequest:
    out: DeleteContactEvaluationRequest = {}  # type: ignore[typeddict-item]
    return out
