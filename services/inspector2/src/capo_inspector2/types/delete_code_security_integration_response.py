"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCodeSecurityIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_integration_arn


class DeleteCodeSecurityIntegrationResponse(TypedDict, closed=True):
    integration_arn: NotRequired[
        "capo_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
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
