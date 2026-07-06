"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCodeSecurityIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_integration_arn
    import aws_sdk_inspector2.types.integration_status


class UpdateCodeSecurityIntegrationResponse(TypedDict, closed=True):
    integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    """<p>The Amazon Resource Name (ARN) of the updated code security integration.</p>"""
    status: "aws_sdk_inspector2.types.integration_status.IntegrationStatus"
    """<p>The current status of the updated code security integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeSecurityIntegrationResponse) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    import aws_sdk_inspector2.types.integration_status

    out["status"] = aws_sdk_inspector2.types.integration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCodeSecurityIntegrationResponse:
    out: UpdateCodeSecurityIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "UpdateCodeSecurityIntegrationResponse.integration_arn required"
        )
    if "status" in data:
        import aws_sdk_inspector2.types.integration_status

        out["status"] = aws_sdk_inspector2.types.integration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "UpdateCodeSecurityIntegrationResponse.status required"
        )
    return out
