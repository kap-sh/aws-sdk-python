"""Generated from Smithy shape ``com.amazonaws.securityagent#GetIntegrationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.integration_id


class GetIntegrationInput(TypedDict):
    integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the integration to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationInput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    return out


def deserialize_json(data: dict) -> GetIntegrationInput:
    out: GetIntegrationInput = {}  # type: ignore[typeddict-item]
    if "integrationId" in data:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("GetIntegrationInput.integration_id required")
    return out
