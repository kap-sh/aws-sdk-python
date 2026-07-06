"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.registry_status


class DeleteRegistryResponse(TypedDict, closed=True):
    status: "aws_sdk_bedrock_agentcore_control.types.registry_status.RegistryStatus"
    """<p>The current status of the registry, set to <code>DELETING</code> when deletion is initiated. For a list of all possible registry statuses, see the <code>RegistryStatus</code> data type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRegistryResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.registry_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteRegistryResponse:
    out: DeleteRegistryResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteRegistryResponse.status required")
    return out
