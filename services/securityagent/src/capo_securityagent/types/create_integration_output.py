"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateIntegrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.integration_id


class CreateIntegrationOutput(TypedDict, closed=True):
    integration_id: "capo_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the created integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationOutput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    return out


def deserialize_json(data: dict) -> CreateIntegrationOutput:
    out: CreateIntegrationOutput = {}  # type: ignore[typeddict-item]
    if "integrationId" in data:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("CreateIntegrationOutput.integration_id required")
    return out
