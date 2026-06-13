"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisterServiceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.additional_service_registration_step
    import aws_sdk_devops_agent.types.kms_key_arn
    import aws_sdk_devops_agent.types.service_id
    import aws_sdk_devops_agent.types.tags


class RegisterServiceOutput(TypedDict):
    service_id: NotRequired["aws_sdk_devops_agent.types.service_id.ServiceId"]
    """<p>Service ID - present when registration is complete, absent when additional steps are required</p>"""
    additional_step: NotRequired[
        "aws_sdk_devops_agent.types.additional_service_registration_step.AdditionalServiceRegistrationStep"
    ]
    """<p>Indicates if additional steps are required to complete service registration (e.g., 3-legged OAuth)</p>"""
    kms_key_arn: NotRequired["aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    tags: NotRequired["aws_sdk_devops_agent.types.tags.Tags"]
    """<p>Tags associated with the registered Service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterServiceOutput) -> dict:
    out: dict = {}
    if "service_id" in value:
        out["serviceId"] = value["service_id"]
    if "additional_step" in value:
        import aws_sdk_devops_agent.types.additional_service_registration_step

        out["additionalStep"] = (
            aws_sdk_devops_agent.types.additional_service_registration_step.serialize_json(
                value["additional_step"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RegisterServiceOutput:
    out: RegisterServiceOutput = {}  # type: ignore[typeddict-item]
    if "serviceId" in data:
        out["service_id"] = data["serviceId"]
    if "additionalStep" in data:
        import aws_sdk_devops_agent.types.additional_service_registration_step

        out["additional_step"] = (
            aws_sdk_devops_agent.types.additional_service_registration_step.deserialize_json(
                data["additionalStep"]
            )
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    return out
