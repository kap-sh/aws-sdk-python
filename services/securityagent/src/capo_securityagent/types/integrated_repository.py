"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedRepository``."""

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError


class IntegratedRepository(TypedDict, closed=True):
    integration_id: "str"
    """<p>The unique identifier of the integration that provides access to the repository.</p>"""
    provider_resource_id: "str"
    """<p>The provider-specific resource identifier for the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedRepository) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["providerResourceId"] = value["provider_resource_id"]
    return out


def deserialize_json(data: dict) -> IntegratedRepository:
    out: IntegratedRepository = {}  # type: ignore[typeddict-item]
    if "integrationId" in data:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("IntegratedRepository.integration_id required")
    if "providerResourceId" in data:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        raise DeserializationError("IntegratedRepository.provider_resource_id required")
    return out
