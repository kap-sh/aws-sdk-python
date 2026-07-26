"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.integrated_resource_metadata
    import capo_securityagent.types.integration_id
    import capo_securityagent.types.provider_resource_capabilities


class IntegratedResourceSummary(TypedDict, closed=True):
    integration_id: "capo_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the integration that provides access to the resource.</p>"""
    resource: "capo_securityagent.types.integrated_resource_metadata.IntegratedResourceMetadata"
    """<p>The metadata for the integrated resource.</p>"""
    capabilities: NotRequired[
        "capo_securityagent.types.provider_resource_capabilities.ProviderResourceCapabilities"
    ]
    """<p>The capabilities enabled for the integrated resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResourceSummary) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    import capo_securityagent.types.integrated_resource_metadata

    out["resource"] = (
        capo_securityagent.types.integrated_resource_metadata.serialize_json(
            value["resource"]
        )
    )
    if "capabilities" in value:
        import capo_securityagent.types.provider_resource_capabilities

        out["capabilities"] = (
            capo_securityagent.types.provider_resource_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegratedResourceSummary:
    out: IntegratedResourceSummary = {}  # type: ignore[typeddict-item]
    if "integrationId" in data:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("IntegratedResourceSummary.integration_id required")
    if "resource" in data:
        import capo_securityagent.types.integrated_resource_metadata

        out["resource"] = (
            capo_securityagent.types.integrated_resource_metadata.deserialize_json(
                data["resource"]
            )
        )
    else:
        raise DeserializationError("IntegratedResourceSummary.resource required")
    if "capabilities" in data:
        import capo_securityagent.types.provider_resource_capabilities

        out["capabilities"] = (
            capo_securityagent.types.provider_resource_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    return out
