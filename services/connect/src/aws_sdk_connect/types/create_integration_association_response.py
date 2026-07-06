"""Generated from Smithy shape ``com.amazonaws.connect#CreateIntegrationAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.integration_association_id


class CreateIntegrationAssociationResponse(TypedDict, closed=True):
    integration_association_id: NotRequired[
        "aws_sdk_connect.types.integration_association_id.IntegrationAssociationId"
    ]
    """<p>The identifier for the integration association.</p>"""
    integration_association_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationAssociationResponse) -> dict:
    out: dict = {}
    if "integration_association_id" in value:
        out["IntegrationAssociationId"] = value["integration_association_id"]
    if "integration_association_arn" in value:
        out["IntegrationAssociationArn"] = value["integration_association_arn"]
    return out


def deserialize_json(data: dict) -> CreateIntegrationAssociationResponse:
    out: CreateIntegrationAssociationResponse = {}  # type: ignore[typeddict-item]
    if "IntegrationAssociationId" in data:
        out["integration_association_id"] = data["IntegrationAssociationId"]
    if "IntegrationAssociationArn" in data:
        out["integration_association_arn"] = data["IntegrationAssociationArn"]
    return out
