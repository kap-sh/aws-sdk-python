"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCodeSecurityIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.authorization_url
    import aws_sdk_inspector2.types.code_security_integration_arn
    import aws_sdk_inspector2.types.integration_status


class CreateCodeSecurityIntegrationResponse(TypedDict, closed=True):
    integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    """<p>The Amazon Resource Name (ARN) of the created code security integration.</p>"""
    status: "aws_sdk_inspector2.types.integration_status.IntegrationStatus"
    """<p>The current status of the code security integration.</p>"""
    authorization_url: NotRequired[
        "aws_sdk_inspector2.types.authorization_url.AuthorizationUrl"
    ]
    """<p>The URL used to authorize the integration with the repository provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSecurityIntegrationResponse) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    import aws_sdk_inspector2.types.integration_status

    out["status"] = aws_sdk_inspector2.types.integration_status.serialize_json(
        value["status"]
    )
    if "authorization_url" in value:
        out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> CreateCodeSecurityIntegrationResponse:
    out: CreateCodeSecurityIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "CreateCodeSecurityIntegrationResponse.integration_arn required"
        )
    if "status" in data:
        import aws_sdk_inspector2.types.integration_status

        out["status"] = aws_sdk_inspector2.types.integration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "CreateCodeSecurityIntegrationResponse.status required"
        )
    if "authorizationUrl" in data:
        out["authorization_url"] = data["authorizationUrl"]
    return out
