"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.approval_configuration
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.registry_arn
    import aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.registry_id
    import aws_sdk_bedrock_agentcore_control.types.registry_name
    import aws_sdk_bedrock_agentcore_control.types.registry_status


class UpdateRegistryResponse(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agentcore_control.types.registry_name.RegistryName"
    """<p>The name of the updated registry.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the updated registry.</p>"""
    registry_id: "aws_sdk_bedrock_agentcore_control.types.registry_id.RegistryId"
    """<p>The unique identifier of the updated registry.</p>"""
    registry_arn: "aws_sdk_bedrock_agentcore_control.types.registry_arn.RegistryArn"
    """<p>The Amazon Resource Name (ARN) of the updated registry.</p>"""
    authorizer_type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"
    ]
    """<p>The type of authorizer used by the updated registry. This controls the authorization method for the Search and Invoke APIs used by consumers.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>"""
    authorizer_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the updated registry. For details, see the <code>AuthorizerConfiguration</code> data type.</p>"""
    approval_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.approval_configuration.ApprovalConfiguration"
    ]
    """<p>The approval configuration for the updated registry. For details, see the <code>ApprovalConfiguration</code> data type.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.registry_status.RegistryStatus"
    """<p>The current status of the updated registry. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, <code>DELETING</code>, and <code>DELETE_FAILED</code>.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the updated registry.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["registryId"] = value["registry_id"]
    out["registryArn"] = value["registry_arn"]
    if "authorizer_type" in value:
        import aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type

        out["authorizerType"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type.serialize_json(
                value["authorizer_type"]
            )
        )
    if "authorizer_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "approval_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.approval_configuration

        out["approvalConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.approval_configuration.serialize_json(
                value["approval_configuration"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types.registry_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_status.serialize_json(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRegistryResponse:
    out: UpdateRegistryResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateRegistryResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    else:
        raise DeserializationError("UpdateRegistryResponse.registry_id required")
    if "registryArn" in data:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError("UpdateRegistryResponse.registry_arn required")
    if "authorizerType" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type

        out["authorizer_type"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    if "authorizerConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if "approvalConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.approval_configuration

        out["approval_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.approval_configuration.deserialize_json(
                data["approvalConfiguration"]
            )
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryResponse.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryResponse.updated_at required")
    return out
