"""Generated from Smithy shape ``com.amazonaws.appintegrations#UpdateDataIntegrationAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_appintegrations.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.execution_configuration
    import aws_sdk_appintegrations.types.identifier

class UpdateDataIntegrationAssociationRequest(TypedDict):
    data_integration_identifier: "aws_sdk_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier for the DataIntegration.</p>"""
    data_integration_association_identifier: "aws_sdk_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier. of the DataIntegrationAssociation resource</p>"""
    execution_configuration: "aws_sdk_appintegrations.types.execution_configuration.ExecutionConfiguration"
    """<p>The configuration for how the files should be pulled from the source.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataIntegrationAssociationRequest) -> dict:
    out: dict = {}
    import aws_sdk_appintegrations.types.execution_configuration
    out["ExecutionConfiguration"] = aws_sdk_appintegrations.types.execution_configuration.serialize_json(value["execution_configuration"])
    return out


def deserialize_json(data: dict) -> UpdateDataIntegrationAssociationRequest:
    out: UpdateDataIntegrationAssociationRequest = {}  # type: ignore[typeddict-item]
    if "ExecutionConfiguration" in data:
        import aws_sdk_appintegrations.types.execution_configuration
        out["execution_configuration"] = aws_sdk_appintegrations.types.execution_configuration.deserialize_json(data["ExecutionConfiguration"])
    else:
        raise DeserializationError("UpdateDataIntegrationAssociationRequest.execution_configuration required")
    return out