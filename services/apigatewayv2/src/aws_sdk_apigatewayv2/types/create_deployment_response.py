"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.__timestamp_iso8601
    import aws_sdk_apigatewayv2.types.deployment_status
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and1024


class CreateDeploymentResponse(TypedDict, closed=True):
    auto_deployed: NotRequired["aws_sdk_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether a deployment was automatically released.</p>"""
    created_date: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time when the Deployment resource was created.</p>"""
    deployment_id: NotRequired["aws_sdk_apigatewayv2.types.id.Id"]
    """<p>The identifier for the deployment.</p>"""
    deployment_status: NotRequired[
        "aws_sdk_apigatewayv2.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the deployment: PENDING, FAILED, or SUCCEEDED.</p>"""
    deployment_status_message: NotRequired[
        "aws_sdk_apigatewayv2.types.__string.__string"
    ]
    """<p>May contain additional feedback on the status of an API deployment.</p>"""
    description: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>The description for the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentResponse) -> dict:
    out: dict = {}
    if "auto_deployed" in value:
        out["autoDeployed"] = value["auto_deployed"]
    if "created_date" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["createdDate"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["created_date"]
            )
        )
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "deployment_status" in value:
        import aws_sdk_apigatewayv2.types.deployment_status

        out["deploymentStatus"] = (
            aws_sdk_apigatewayv2.types.deployment_status.serialize_json(
                value["deployment_status"]
            )
        )
    if "deployment_status_message" in value:
        out["deploymentStatusMessage"] = value["deployment_status_message"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentResponse:
    out: CreateDeploymentResponse = {}  # type: ignore[typeddict-item]
    if "autoDeployed" in data:
        out["auto_deployed"] = data["autoDeployed"]
    if "createdDate" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["created_date"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["createdDate"]
            )
        )
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "deploymentStatus" in data:
        import aws_sdk_apigatewayv2.types.deployment_status

        out["deployment_status"] = (
            aws_sdk_apigatewayv2.types.deployment_status.deserialize_json(
                data["deploymentStatus"]
            )
        )
    if "deploymentStatusMessage" in data:
        out["deployment_status_message"] = data["deploymentStatusMessage"]
    if "description" in data:
        out["description"] = data["description"]
    return out
