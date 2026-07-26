"""Generated from Smithy shape ``com.amazonaws.appintegrations#UpdateDataIntegrationAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appintegrations.types.execution_configuration
    import capo_appintegrations.types.identifier


class UpdateDataIntegrationAssociationRequest(TypedDict, closed=True):
    data_integration_identifier: "capo_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier for the DataIntegration.</p>"""
    data_integration_association_identifier: (
        "capo_appintegrations.types.identifier.Identifier"
    )
    """<p>A unique identifier. of the DataIntegrationAssociation resource</p>"""
    execution_configuration: (
        "capo_appintegrations.types.execution_configuration.ExecutionConfiguration"
    )
    """<p>The configuration for how the files should be pulled from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataIntegrationAssociationRequest) -> dict:
    out: dict = {}
    import capo_appintegrations.types.execution_configuration

    out["ExecutionConfiguration"] = (
        capo_appintegrations.types.execution_configuration.serialize_json(
            value["execution_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDataIntegrationAssociationRequest:
    out: UpdateDataIntegrationAssociationRequest = {}  # type: ignore[typeddict-item]
    if "ExecutionConfiguration" in data:
        import capo_appintegrations.types.execution_configuration

        out["execution_configuration"] = (
            capo_appintegrations.types.execution_configuration.deserialize_json(
                data["ExecutionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataIntegrationAssociationRequest.execution_configuration required"
        )
    return out
