"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCodeSecurityIntegrationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_integration_arn


class DeleteCodeSecurityIntegrationResponse(TypedDict):
    integration_arn: NotRequired[
        "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the deleted code security integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeSecurityIntegrationResponse) -> dict:
    out: dict = {}
    if "integration_arn" in value:
        out["integrationArn"] = value["integration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteCodeSecurityIntegrationResponse:
    out: DeleteCodeSecurityIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    return out
