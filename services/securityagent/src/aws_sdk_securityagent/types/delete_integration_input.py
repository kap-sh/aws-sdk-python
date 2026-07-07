"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.integration_id


class DeleteIntegrationInput(TypedDict, closed=True):
    integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the integration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntegrationInput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    return out


def deserialize_json(data: dict) -> DeleteIntegrationInput:
    out: DeleteIntegrationInput = {}  # type: ignore[typeddict-item]
    if "integrationId" in data:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("DeleteIntegrationInput.integration_id required")
    return out
