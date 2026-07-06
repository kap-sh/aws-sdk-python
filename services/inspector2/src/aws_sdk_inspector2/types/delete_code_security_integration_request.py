"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCodeSecurityIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_integration_arn


class DeleteCodeSecurityIntegrationRequest(TypedDict, closed=True):
    integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    """<p>The Amazon Resource Name (ARN) of the code security integration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeSecurityIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteCodeSecurityIntegrationRequest:
    out: DeleteCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "DeleteCodeSecurityIntegrationRequest.integration_arn required"
        )
    return out
