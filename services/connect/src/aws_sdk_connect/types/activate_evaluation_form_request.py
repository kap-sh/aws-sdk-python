"""Generated from Smithy shape ``com.amazonaws.connect#ActivateEvaluationFormRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.version_number


class ActivateEvaluationFormRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    evaluation_form_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: "aws_sdk_connect.types.version_number.VersionNumber"
    """<p>The version of the evaluation form to activate. If the version property is not provided, the latest version of the evaluation form is activated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateEvaluationFormRequest) -> dict:
    out: dict = {}
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    return out


def deserialize_json(data: dict) -> ActivateEvaluationFormRequest:
    out: ActivateEvaluationFormRequest = {}  # type: ignore[typeddict-item]
    if "EvaluationFormVersion" in data:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    return out
