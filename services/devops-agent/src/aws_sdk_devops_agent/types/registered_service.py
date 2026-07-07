"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.additional_service_details
    import aws_sdk_devops_agent.types.document_list
    import aws_sdk_devops_agent.types.kms_key_arn
    import aws_sdk_devops_agent.types.private_connection_name
    import aws_sdk_devops_agent.types.service
    import aws_sdk_devops_agent.types.service_id
    import aws_sdk_devops_agent.types.service_name


class RegisteredService(TypedDict, closed=True):
    service_id: "aws_sdk_devops_agent.types.service_id.ServiceId"
    """<p>The unique identifier of a service.</p>"""
    service_type: "aws_sdk_devops_agent.types.service.Service"
    """<p>The service type e.g github or dynatrace</p>"""
    name: NotRequired["aws_sdk_devops_agent.types.service_name.ServiceName"]
    """<p>The display name of the registered service.</p>"""
    accessible_resources: NotRequired[
        "aws_sdk_devops_agent.types.document_list.DocumentList"
    ]
    """<p>List of accessible resources for this service.</p>"""
    additional_service_details: NotRequired[
        "aws_sdk_devops_agent.types.additional_service_details.AdditionalServiceDetails"
    ]
    """<p>Additional details specific to the service type.</p>"""
    kms_key_arn: NotRequired["aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    private_connection_name: NotRequired[
        "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection used for VPC connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredService) -> dict:
    out: dict = {}
    out["serviceId"] = value["service_id"]
    import aws_sdk_devops_agent.types.service

    out["serviceType"] = aws_sdk_devops_agent.types.service.serialize_json(
        value["service_type"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "accessible_resources" in value:
        import aws_sdk_devops_agent.types.document_list

        out["accessibleResources"] = (
            aws_sdk_devops_agent.types.document_list.serialize_json(
                value["accessible_resources"]
            )
        )
    if "additional_service_details" in value:
        import aws_sdk_devops_agent.types.additional_service_details

        out["additionalServiceDetails"] = (
            aws_sdk_devops_agent.types.additional_service_details.serialize_json(
                value["additional_service_details"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "private_connection_name" in value:
        out["privateConnectionName"] = value["private_connection_name"]
    return out


def deserialize_json(data: dict) -> RegisteredService:
    out: RegisteredService = {}  # type: ignore[typeddict-item]
    if "serviceId" in data:
        out["service_id"] = data["serviceId"]
    else:
        raise DeserializationError("RegisteredService.service_id required")
    if "serviceType" in data:
        import aws_sdk_devops_agent.types.service

        out["service_type"] = aws_sdk_devops_agent.types.service.deserialize_json(
            data["serviceType"]
        )
    else:
        raise DeserializationError("RegisteredService.service_type required")
    if "name" in data:
        out["name"] = data["name"]
    if "accessibleResources" in data:
        import aws_sdk_devops_agent.types.document_list

        out["accessible_resources"] = (
            aws_sdk_devops_agent.types.document_list.deserialize_json(
                data["accessibleResources"]
            )
        )
    if "additionalServiceDetails" in data:
        import aws_sdk_devops_agent.types.additional_service_details

        out["additional_service_details"] = (
            aws_sdk_devops_agent.types.additional_service_details.deserialize_json(
                data["additionalServiceDetails"]
            )
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "privateConnectionName" in data:
        out["private_connection_name"] = data["privateConnectionName"]
    return out
