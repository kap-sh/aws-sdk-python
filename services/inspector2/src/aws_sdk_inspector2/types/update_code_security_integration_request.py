"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCodeSecurityIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_integration_arn
    import aws_sdk_inspector2.types.update_integration_details


class UpdateCodeSecurityIntegrationRequest(TypedDict, closed=True):
    integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    """<p>The Amazon Resource Name (ARN) of the code security integration to update.</p>"""
    details: (
        "aws_sdk_inspector2.types.update_integration_details.UpdateIntegrationDetails"
    )
    """<p>The updated integration details specific to the repository provider type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeSecurityIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    import aws_sdk_inspector2.types.update_integration_details

    out["details"] = aws_sdk_inspector2.types.update_integration_details.serialize_json(
        value["details"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCodeSecurityIntegrationRequest:
    out: UpdateCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "UpdateCodeSecurityIntegrationRequest.integration_arn required"
        )
    if "details" in data:
        import aws_sdk_inspector2.types.update_integration_details

        out["details"] = (
            aws_sdk_inspector2.types.update_integration_details.deserialize_json(
                data["details"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCodeSecurityIntegrationRequest.details required"
        )
    return out
