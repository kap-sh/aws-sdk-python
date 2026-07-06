"""Generated from Smithy shape ``com.amazonaws.appintegrations#CreateDataIntegrationAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.uuid


class CreateDataIntegrationAssociationResponse(TypedDict, closed=True):
    data_integration_association_id: NotRequired[
        "aws_sdk_appintegrations.types.uuid.UUID"
    ]
    """<p>A unique identifier. for the DataIntegrationAssociation.</p>"""
    data_integration_arn: NotRequired["aws_sdk_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the DataIntegration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataIntegrationAssociationResponse) -> dict:
    out: dict = {}
    if "data_integration_association_id" in value:
        out["DataIntegrationAssociationId"] = value["data_integration_association_id"]
    if "data_integration_arn" in value:
        out["DataIntegrationArn"] = value["data_integration_arn"]
    return out


def deserialize_json(data: dict) -> CreateDataIntegrationAssociationResponse:
    out: CreateDataIntegrationAssociationResponse = {}  # type: ignore[typeddict-item]
    if "DataIntegrationAssociationId" in data:
        out["data_integration_association_id"] = data["DataIntegrationAssociationId"]
    if "DataIntegrationArn" in data:
        out["data_integration_arn"] = data["DataIntegrationArn"]
    return out
